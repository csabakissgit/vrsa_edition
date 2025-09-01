$(function () {
    function getTemplate(template, data) {
        if (template == 'photo') {
            return `
                    <div class="col-md-4" style="margin-bottom:30px">
                        <a href="${data.slug}">
                            <div class="card ecs-card">
                                <img style="height:300px;"
                                        class="lazyload card-img w-100 img-fluid rounded-0"
                                        data-sizes="auto"
                                        data-src="${data.image}"/>
                                <div  class="card-img-overlay d-flex align-items-end">
                                    <h4 class="card-title ecs-article-title">${data.title}</h4>
                                </div>
                            </div>
                        </a>
                    </div>
                `;
        }

        if (template == 'post') {
            return `
            <div class="col-md-4" style="margin-bottom:40px;">
						<article class="card ecs-card">
							<header class="card-header p-0 border-0">
								<a href="${data.slug}" class="img" title="${data.title}">
                                    <img
                                    style="height:220px;"
                                    class="lazyload card-img w-100 img-fluid rounded-0"
                                    data-sizes="auto"
                                    data-src="${data.thumbnail}" alt="${data.title}">
								</a>
								<a href="${data.slug}" title="${data.title}">
									<h4 class="card-title ecs-article-title">${data.title}</h4>
								</a>
							</header>

							<div class="card-body">
								 <div class="ecs-tags">
									<span class="ecs-tags--published-date">${data.date}</span>
									<a href="${data.issue_link}" class="ecs-tags--issue-number">Issue ${data.issue_no}</a>
									<a href="${data.author_link}">${data.author}</a>
								</div>
								<div class="card-description ecs-article-description">
									<p>${data.content}</p>
								</div>
							</div>
						</article>
					</div>
            `;
        }
    }

    var loading = false;
    var total = 0;
    var loadButton = $('#loadMore');
    var perPage = 0;
    var offset = 0;
    var buttonText = '';
    var container = '';
    var template = '';

    var onError = function () {
    }

    var onSuccess = function (data) {
        offset += perPage;

        var html = '';
        for (var i = 0; i < data.length; i++) {
            html += getTemplate(template, data[i]);
        }

        $(container).append(html);
    }

    var onComplete = function () {
        loadButton.text(buttonText);
        loading = false;
        if (offset >= total) {
            loadButton.hide();
        }
    }

    loadButton.on('click', function (e) {
        e.preventDefault();
        if (loading) return;
        var ajaxURL = $(this).data('url');
        total = parseInt($(this).data('total'));
        perPage = parseInt($(this).data('perpage'));
        template = $(this).data('template');

        if (offset === 0) {
            offset = perPage;
        }

        container = $(this).data('container');
        buttonText = $(this).text();
        loading = true;
        loadButton.text('loading...');
        $.ajax({
            url: ajaxURL,
            dataType: 'json',
            data: { skip: offset, limit: perPage },
        }).done(onSuccess)
            .fail(onError)
            .always(onComplete);
    });
});


$(document).ready(function () {
    //search
    var search = $('#ecs-search'),
        input = search.find('input.ecs-search-input'),
        ctrlClose = search.find('span.ecs-search-close'),
        isOpen = isAnimating = false,
        searchButton = $('#btn-ecs-search, #btn-ecs-search--xs');
    // show/hide search area
    toggleSearch = function (evt) {
        // return if open and the input gets focused
        if (evt.type.toLowerCase() === 'focus' && isOpen) return false;

        if (isOpen) {
            search.removeClass('open')

            // trick to hide input text once the search overlay closes
            // todo: hardcoded times, should be done after transition ends
            if (input.value !== '') {
                setTimeout(function () {
                    search.addClass('hideInput');
                    setTimeout(function () {
                        search.removeClass('hideInput');
                        input.value = '';
                    }, 300);
                }, 500);
            }

            input.blur();
        } else {
            search.addClass('open')
        }

        isOpen = !isOpen;
    };

    searchButton.on('click', toggleSearch);
    ctrlClose.on('click', toggleSearch);

    // esc key closes search overlay
    // keyboard navigation events
    $(document).on('keydown', function (ev) {
        var keyCode = ev.keyCode || ev.which;
        if (keyCode === 27 && isOpen) {
            toggleSearch(ev);
        }
    });

    // Check if element is scrolled into view
    function isScrolledIntoView(elem) {
        var docViewTop = $(window).scrollTop();
        var docViewBottom = docViewTop + $(window).height();

        var elemTop = $(elem).offset().top;
        var elemBottom = elemTop + $(elem).height();

        return (elemTop >= docViewTop && elemTop <= docViewBottom) || (elemBottom >= docViewTop && elemBottom <= docViewBottom);
    }

    // animation
    // If element is scrolled into view, fade it in
    function animate() {
        $('.animated').each(function () {
            if (isScrolledIntoView(this) === true) {
                $(this).addClass($(this).data('animation'));
                $(this).addClass('animated-show');
            }
        });
    }
    animate();
    $(window).scroll(animate);
});


$(function(){
    $('.slider').slick({
        dots: false,
        infinite: true,
        speed: 300,
        slidesToShow: 1,
        centerMode: true,
        variableWidth: true
    });

    $('.request-reservation').on('click', function(e){
        e.preventDefault();
        $('html, body').animate({
            scrollTop: $('#form-request').offset().top - 50
        }, 500);
    })

    $('#form-request').on('submit', function (e) {
        e.preventDefault();
        var mapping = {
            full_name: "Full Name",
            address: 'Address',
            phone: 'Phone',
            email: 'Email',
            nationality: 'Nationality',
            no_of_pax: 'No. of Pax',
            option: 'This field'
        }
        $('.alert').remove();
        var fields = $(this).serializeArray();
        if ($(this).serializeArray().length === 6) {
            fields.push({ name: 'option', value: '' });
        }
        var error = 0;
        $.each(fields, function (i, field) {
            if (field.value.trim() === '') {
                $("#" + field.name).after("<div class='alert alert-danger'>" + mapping[field.name] + " is required.</div>");
                error++;
            }
        });

        if (error > 0) return;
        $('.btn-default').text('Loading');
        $('.btn-default').prop("disabled", true);
        var $this = $(this);
        $.ajax({
            method: "POST",
            url: $(this).prop('action'),
            data: $(this).serializeArray(),
            dataType: 'json'
        }).done(function () {
            $this.before('<div class="alert alert-success">Your request has been sent. We\'ll get back to you soon.</div>')
            $this.trigger("reset");
        })
            .fail(function () {
                $this.before('<div class="alert alert-danger">Oops Something went wrong, please try again.</div>')
            })
            .always(function () {
                $('.btn-default').text('Submit');
                $('.btn-default').prop('disabled', false);
                $('html, body').animate({
                    scrollTop: $this.offset().top - 100
                }, 500);
            });
    });
});