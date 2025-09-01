
'''
bib_substitutions.py
Deals with <cite>BLA</cite> and <citep>BLA</cite> bibliographical references in .cred files
'''

import re

bib_dict = [{"ref": "KaneHistory", "short": "Kane 1930–1962", "full": "Kane, Pandurang Vaman. 1930–1962. <i>History of Dharmaśāstra</i> Poona: Bhandarkar Oriental Research Institute."},
            {"ref":"Mylius", "short": "Mylius 1995.", "full":"Mylius, Klaus 1995. <i>Wörterbuch des altindischen Rituals: mit einer Übersicht über das altindische Opferritual und einem Plan der Opferstätte.</i> Wichtrach: Institut für Indologie."},
            {"ref": "KafleKrsnastami", "short": "Kafle 2019", "full": "Kafle, Nirajan. 2019. 'The <i>kṛṣṇāṣṭamīvrata</i> in the Śivadharmaśāstra. A Comparative Edition and Study.' <i>Indo-Iranian Journal</i> 62: 340–383."},
            {"ref": "KafleNisvasaBook", "short": "Kafle 2020", "full": "Kafle, Nirajan 2020. <i>Niśvāsamukhatattvasamhitā. A Preface to the Earliest Surviving Śaiva Tantra.</i> Collection Indologie 145. Pondicherry: Institut Français de Pondichéry; École Française d'Extrême-Orient."},
            {"ref": "VaidyaManjusri", "short": "Vaidya 1964", "full": "Vaidya, P. L. (ed.). 1964. <i>Mahāyānasūtrasaṃgraha. Part 2. Buddhist Sanskrit Texts 18.</i> Darbhanga: The Mithila Institute."},
            {"ref":"Vinayasutra", "short": "Yoshiyasu 2020", "full": "Yoshiyasu, Yonezawa. 2020.  <i>Vinayasūtra. Preliminary transliteration of the ms. found in Tibet by Rahula Sankrityayana.  (Bhadantaguṇaprabhaviracitaṃ [mūlasarvāstivādīyaṃ] vinayasūtram).</i> GRETIL e-text."},
    {"ref":"SearsWorldly2014", "short": "Sears 2014", "full": "Sears, Tamara~I. 2014. <i>Worldly Gurus and Spiritual Kings: Architecture and Asceticism in Medieval India.</i> New Haven: Yale University Press."},
    {"ref":"KumarasambhavaSmith", "short": "Smith 2005", "full": "Smith, David (tr.). 2005.  <i>The Birth of Kumāra by Kālidāsa.</i> New York University Press, JCC Foundation."},
    {"ref":"SDhU02Florinda", "short": "ŚDhU 2", "full": "De Simini, Florinda (forthcoming).  <i>Critical Edition and Translation of Śivadharmottara 2–4.</i>"},
            {"ref":"HCCTorzsok", "short": "Törzsök (forthcoming)", "full":"Törzsök, Judit. (forthcoming).  <i>Śivadharma in Kashmir. A Critical Edition of Chapters 17, and 29–30 of the Haracaritacintāmaṇi.</i> Napoli: UniorPress."},
            {"ref":"YokochiSaivaCosmogr", "short": "Yokochi 2021", "full":"Yokochi, Yuko. 2021. 'Śaiva cosmography in the Śivadharmottara.' In <i>Śivadharmāmṛta. Essays on the Śivadharma and its Network</i>, edited by Florinda De~Simini and Csaba Kiss. Studies on the History of Śaivism 2. Università di Napoli L’Orientale Dipartimento Asia, Africa e Mediterraneo, Napoli: UniorPress. 73–99."},
{"ref":"SDHU12Yuko","short": "Yokochi 2023", "full": "Yokochi, Yuko. 2023. 'Śivadharmottara 12 (draft critical edition)."},
{"ref":"YagiBhaksya", "short": "Yagi 1994", "full": "Yagi, Toru. 1994.  'A Note on bhojya- and bhakṣya-.' In <i>A Study of the Nīlamata. Aspects of Hinduism in Ancient Kashmir</i>, edited by Yasuke Ikari. Kyoto: Institute for Research in Humanities, Kyoto University. 377–397."},
{"ref": "GlossVeg", "short": "Singhand Chunekar 1999", "full": "Singh, Thakur Balwant, and K. C. Chunekar. 1999.  <i>Glossary of Vegetable Drugs in Brhattrayī.</i> Varanasi: Chaukhambha Amarabharati Prakashan."},
{"ref":"Meulenbeld1974", "short": "Meulenbeld 1974", "full": "Meulenbeld, G. J. 1974.  <i>The Mādhavanidāna and its Chief Commentary: Chapters 1–10.</i> Leiden: E. J. Brill."},
{"ref":"GeslaniGodking", "short": "Geslani 2018.", "full": "Geslani, Marko. 2018.  <i>Rites of the God-King: Śānti and Ritual Change in Early Hinduism.</i> Oxford University Press."},
{"ref":"OlivelleManu", "short": "Olivelle 2005", "full": "Olivelle, Patrick. 2005.  <i>Manu's Code of Law: a critical edition and translation of the Mānava-Dharmaśāstra.</i> New York: Oxford University Press."},
{"ref": "SaivaUtopia2021", "short": "Bisschop et al. 2021", "full": "Bisschop, Peter C., Nirajan Kafle, and Timothy Lubin. 2021.  <i>A Śaiva Utopia. The Śivadharma's Revision of Brahmanical Varṇāśramadharma. Critical Edition, Translation & Study of the Śivāśramādhyāya of the Śivadharmaśāstra.</i> Studies in the History of Śaivism I. Napoli: Università degli Studi di Napoli L'Orientale, Dipartimento Asia, Africa e Mediterraneo."},
{"ref":"JacobiComputation", "short": "Jacobi 1892", "full": "Jacobi, Hermann. 1892.  'The computation of Hindu dates in inscriptions &c..' <i>Epigraphia Indica</i> 1: 403–360."},
{"ref":"SandersonExegesis", "short": "Sanderson 2007", "full": "Sanderson, Alexis 2007. 'The Śaiva Exegesis of Kashmir.  In <i>Mélenges tantriques à la memoir d'Hélène Brunner / Tantric Studies in Memory of Hélène Brunner</i>, edited by Dominic Goodall and André Padoux. Pondicherry: IFP / EFEO. 231–442."},
{"ref":"Parasara2-1", "short": "Islāmpurkar 1898", "full": "Islāmpurkar, Vāman Śāstri (ed.). 1898.  <i>The Parâśara Dharma Samhita Or Parāśara Smṛiti with the Commentary of Sâyaṇa Mâdhavâchârya. Volume 2, Part 1.</i> Bombay Sanskrit Series~59. Bombay: Government Central Book Depot."},
{"ref":"KissVSS", "short": "Kiss. 2025 [forthcoming]", "full": "Kiss, Csaba. 2025 [forthcoming].  <i>The Vṛṣasārasaṃgraha. Volume 1.</i> Studies in the History of Śaivism. Napoli: Università degli Studi di Napoli L'Orientale, Dipartimento Asia, Africa e Mediterraneo, UniorPress."}]


def main(text):
    for reference in bib_dict:
        text = re.sub('<cite>' + reference["ref"] + '</cite>',  '<div class="bibtooltip"><cite>' +  reference["short"] + '</cite><span class="bibtooltiptext">' + reference["full"] + '</span></div>', text)
        text = re.sub('<citep>' + reference["ref"] + '</citep>', '<div class="bibtooltip"><citep>' + reference["short"] + '</citep><span class="bibtooltiptext">' + reference["full"] + '</span></div>', text)
    return text


