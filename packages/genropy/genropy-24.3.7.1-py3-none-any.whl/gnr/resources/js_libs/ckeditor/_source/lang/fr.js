﻿/*
Copyright (c) 2003-2013, CKSource - Frederico Knabben. All rights reserved.
For licensing, see LICENSE.html or http://ckeditor.com/license
*/

/**
 * @fileOverview Defines the {@link CKEDITOR.lang} object, for the
 * French language.
 */

/**#@+
   @type String
   @example
*/

/**
 * Contains the dictionary of language entries.
 * @namespace
 */
CKEDITOR.lang['fr'] =
{
	/**
	 * The language reading direction. Possible values are "rtl" for
	 * Right-To-Left languages (like Arabic) and "ltr" for Left-To-Right
	 * languages (like English).
	 * @default 'ltr'
	 */
	dir : 'ltr',

	/*
	 * Screenreader titles. Please note that screenreaders are not always capable
	 * of reading non-English words. So be careful while translating it.
	 */
	editorTitle : 'Éditeur de Texte Enrichi, %1',
	editorHelp : 'Appuyez sur ALT-0 pour l\'aide',

	// ARIA descriptions.
	toolbars	: 'Barre d\'outils de l\'éditeur',
	editor		: 'Éditeur de Texte Enrichi',

	// Toolbar buttons without dialogs.
	source			: 'Source',
	newPage			: 'Nouvelle page',
	save			: 'Enregistrer',
	preview			: 'Aperçu',
	cut				: 'Couper',
	copy			: 'Copier',
	paste			: 'Coller',
	print			: 'Imprimer',
	underline		: 'Souligné',
	bold			: 'Gras',
	italic			: 'Italique',
	selectAll		: 'Tout sélectionner',
	removeFormat	: 'Supprimer la mise en forme',
	strike			: 'Barré',
	subscript		: 'Indice',
	superscript		: 'Exposant',
	horizontalrule	: 'Ligne horizontale',
	pagebreak		: 'Saut de page',
	pagebreakAlt		: 'Saut de page',
	unlink			: 'Supprimer le lien',
	undo			: 'Annuler',
	redo			: 'Rétablir',

	// Common messages and labels.
	common :
	{
		browseServer	: 'Explorer le serveur',
		url				: 'URL',
		protocol		: 'Protocole',
		upload			: 'Envoyer',
		uploadSubmit	: 'Envoyer sur le serveur',
		image			: 'Image',
		flash			: 'Flash',
		form			: 'Formulaire',
		checkbox		: 'Case à cocher',
		radio			: 'Bouton Radio',
		textField		: 'Champ texte',
		textarea		: 'Zone de texte',
		hiddenField		: 'Champ caché',
		button			: 'Bouton',
		select			: 'Liste déroulante',
		imageButton		: 'Bouton image',
		notSet			: '<non défini>',
		id				: 'Id',
		name			: 'Nom',
		langDir			: 'Sens d\'écriture',
		langDirLtr		: 'Gauche à droite (LTR)',
		langDirRtl		: 'Droite à gauche (RTL)',
		langCode		: 'Code de langue',
		longDescr		: 'URL de description longue (longdesc => malvoyant)',
		cssClass		: 'Classe CSS',
		advisoryTitle	: 'Description (title)',
		cssStyle		: 'Style',
		ok				: 'OK',
		cancel			: 'Annuler',
		close			: 'Fermer',
		preview			: 'Aperçu',
		generalTab		: 'Général',
		advancedTab		: 'Avancé',
		validateNumberFailed : 'Cette valeur n\'est pas un nombre.',
		confirmNewPage	: 'Les changements non sauvegardés seront perdus. Êtes-vous sûr de vouloir charger une nouvelle page?',
		confirmCancel	: 'Certaines options ont été modifiées. Êtes-vous sûr de vouloir fermer?',
		options			: 'Options',
		target			: 'Cible (Target)',
		targetNew		: 'Nouvelle fenêtre (_blank)',
		targetTop		: 'Fenêtre supérieure (_top)',
		targetSelf		: 'Même fenêtre (_self)',
		targetParent	: 'Fenêtre parent (_parent)',
		langDirLTR		: 'Gauche à Droite (LTR)',
		langDirRTL		: 'Droite à Gauche (RTL)',
		styles			: 'Style',
		cssClasses		: 'Classes de style',
		width			: 'Largeur',
		height			: 'Hauteur',
		align			: 'Alignement',
		alignLeft		: 'Gauche',
		alignRight		: 'Droite',
		alignCenter		: 'Centré',
		alignTop		: 'Haut',
		alignMiddle		: 'Milieu',
		alignBottom		: 'Bas',
		invalidValue	: 'Invalid value.', // MISSING
		invalidHeight	: 'La hauteur doit être un nombre.',
		invalidWidth	: 'La largeur doit être un nombre.',
		invalidCssLength	: 'La valeur spécifiée pour le champ "%1" doit être un nombre positif avec ou sans unité de mesure CSS valide (px, %, in, cm, mm, em, ex, pt, or pc).',
		invalidHtmlLength	: 'La valeur spécifiée pour le champ "%1" doit être un nombre positif avec ou sans unité de mesure HTML valide (px or %).',
		invalidInlineStyle	: 'La valeur spécifiée pour le style inline doit être composée d\'un ou plusieurs couples de valeur au format "nom : valeur", separés par des points-virgules.',
		cssLengthTooltip	: 'Entrer un nombre pour une valeur en pixels ou un nombre avec une unité de mesure CSS valide (px, %, in, cm, mm, em, ex, pt, or pc).',

		// Put the voice-only part of the label in the span.
		unavailable		: '%1<span class="cke_accessibility">, Indisponible</span>'
	},

	contextmenu :
	{
		options : 'Options du menu contextuel'
	},

	// Special char dialog.
	specialChar		:
	{
		toolbar		: 'Insérer un caractère spécial',
		title		: 'Sélectionnez un caractère',
		options : 'Options des caractères spéciaux'
	},

	// Link dialog.
	link :
	{
		toolbar		: 'Lien',
		other 		: '<autre>',
		menu		: 'Editer le lien',
		title		: 'Lien',
		info		: 'Infos sur le lien',
		target		: 'Cible',
		upload		: 'Envoyer',
		advanced	: 'Avancé',
		type		: 'Type de lien',
		toUrl		: 'URL',
		toAnchor	: 'Transformer le lien en ancre dans le texte',
		toEmail		: 'E-mail',
		targetFrame		: '<cadre>',
		targetPopup		: '<fenêtre popup>',
		targetFrameName	: 'Nom du Cadre destination',
		targetPopupName	: 'Nom de la fenêtre popup',
		popupFeatures	: 'Options de la fenêtre popup',
		popupResizable	: 'Redimensionnable',
		popupStatusBar	: 'Barre de status',
		popupLocationBar: 'Barre d\'adresse',
		popupToolbar	: 'Barre d\'outils',
		popupMenuBar	: 'Barre de menu',
		popupFullScreen	: 'Plein écran (IE)',
		popupScrollBars	: 'Barres de défilement',
		popupDependent	: 'Dépendante (Netscape)',
		popupLeft		: 'Position gauche',
		popupTop		: 'Position haute',
		id				: 'Id',
		langDir			: 'Sens d\'écriture',
		langDirLTR		: 'Gauche à droite',
		langDirRTL		: 'Droite à gauche',
		acccessKey		: 'Touche d\'accessibilité',
		name			: 'Nom',
		langCode			: 'Code de langue',
		tabIndex			: 'Index de tabulation',
		advisoryTitle		: 'Description (title)',
		advisoryContentType	: 'Type de contenu (ex: text/html)',
		cssClasses		: 'Classe CSS',
		charset			: 'Charset de la cible',
		styles			: 'Style',
		rel			: 'Relation',
		selectAnchor		: 'Sélectionner l\'ancre',
		anchorName		: 'Par nom d\'ancre',
		anchorId			: 'Par ID d\'élément',
		emailAddress		: 'Adresse E-Mail',
		emailSubject		: 'Sujet du message',
		emailBody		: 'Corps du message',
		noAnchors		: '(Aucune ancre disponible dans ce document)',
		noUrl			: 'Veuillez entrer l\'adresse du lien',
		noEmail			: 'Veuillez entrer l\'adresse e-mail'
	},

	// Anchor dialog
	anchor :
	{
		toolbar		: 'Ancre',
		menu		: 'Editer l\'ancre',
		title		: 'Propriétés de l\'ancre',
		name		: 'Nom de l\'ancre',
		errorName	: 'Veuillez entrer le nom de l\'ancre.',
		remove		: 'Supprimer l\'ancre'
	},

	// List style dialog
	list:
	{
		numberedTitle		: 'Propriétés de la liste numérotée',
		bulletedTitle		: 'Propriétés de la liste à puces',
		type				: 'Type',
		start				: 'Début',
		validateStartNumber				:'Le premier élément de la liste doit être un nombre entier.',
		circle				: 'Cercle',
		disc				: 'Disque',
		square				: 'Carré',
		none				: 'Aucun',
		notset				: '<Non défini>',
		armenian			: 'Numération arménienne',
		georgian			: 'Numération géorgienne (an, ban, gan, etc.)',
		lowerRoman			: 'Nombres romains minuscules (i, ii, iii, iv, v, etc.)',
		upperRoman			: 'Nombres romains majuscules (I, II, III, IV, V, etc.)',
		lowerAlpha			: 'Alphabétique minuscules (a, b, c, d, e, etc.)',
		upperAlpha			: 'Alphabétique majuscules (A, B, C, D, E, etc.)',
		lowerGreek			: 'Grec minuscule (alpha, beta, gamma, etc.)',
		decimal				: 'Décimal (1, 2, 3, etc.)',
		decimalLeadingZero	: 'Décimal précédé par un 0 (01, 02, 03, etc.)'
	},

	// Find And Replace Dialog
	findAndReplace :
	{
		title				: 'Trouver et remplacer',
		find				: 'Trouver',
		replace				: 'Remplacer',
		findWhat			: 'Expression à trouver: ',
		replaceWith			: 'Remplacer par: ',
		notFoundMsg			: 'Le texte spécifié ne peut être trouvé.',
		findOptions			: 'Options de recherche',
		matchCase			: 'Respecter la casse',
		matchWord			: 'Mot entier uniquement',
		matchCyclic			: 'Boucler',
		replaceAll			: 'Remplacer tout',
		replaceSuccessMsg	: '%1 occurrence(s) replacée(s).'
	},

	// Table Dialog
	table :
	{
		toolbar		: 'Tableau',
		title		: 'Propriétés du tableau',
		menu		: 'Propriétés du tableau',
		deleteTable	: 'Supprimer le tableau',
		rows		: 'Lignes',
		columns		: 'Colonnes',
		border		: 'Taille de la bordure',
		widthPx		: 'pixels',
		widthPc		: '% pourcents',
		widthUnit	: 'unité de largeur',
		cellSpace	: 'Espacement des cellules',
		cellPad		: 'Marge interne des cellules',
		caption		: 'Titre du tableau',
		summary		: 'Résumé (description)',
		headers		: 'En-Têtes',
		headersNone		: 'Aucunes',
		headersColumn	: 'Première colonne',
		headersRow		: 'Première ligne',
		headersBoth		: 'Les deux',
		invalidRows		: 'Le nombre de lignes doit être supérieur à 0.',
		invalidCols		: 'Le nombre de colonnes doit être supérieur à 0.',
		invalidBorder	: 'La taille de la bordure doit être un nombre.',
		invalidWidth	: 'La largeur du tableau doit être un nombre.',
		invalidHeight	: 'La hauteur du tableau doit être un nombre.',
		invalidCellSpacing	: 'L\'espacement des cellules doit être un nombre positif.',
		invalidCellPadding	: 'La marge intérieure des cellules doit être un nombre positif.',

		cell :
		{
			menu			: 'Cellule',
			insertBefore	: 'Insérer une cellule avant',
			insertAfter		: 'Insérer une cellule après',
			deleteCell		: 'Supprimer les cellules',
			merge			: 'Fusionner les cellules',
			mergeRight		: 'Fusionner à droite',
			mergeDown		: 'Fusionner en bas',
			splitHorizontal	: 'Fractionner horizontalement',
			splitVertical	: 'Fractionner verticalement',
			title			: 'Propriétés de la cellule',
			cellType		: 'Type de cellule',
			rowSpan			: 'Fusion de lignes',
			colSpan			: 'Fusion de colonnes',
			wordWrap		: 'Césure',
			hAlign			: 'Alignement Horizontal',
			vAlign			: 'Alignement Vertical',
			alignBaseline	: 'Bas du texte',
			bgColor			: 'Couleur d\'arrière-plan',
			borderColor		: 'Couleur de Bordure',
			data			: 'Données',
			header			: 'Entête',
			yes				: 'Oui',
			no				: 'Non',
			invalidWidth	: 'La Largeur de Cellule doit être un nombre.',
			invalidHeight	: 'La Hauteur de Cellule doit être un nombre.',
			invalidRowSpan	: 'La fusion de lignes doit être un nombre entier.',
			invalidColSpan	: 'La fusion de colonnes doit être un nombre entier.',
			chooseColor		: 'Choisissez'
		},

		row :
		{
			menu			: 'Ligne',
			insertBefore	: 'Insérer une ligne avant',
			insertAfter		: 'Insérer une ligne après',
			deleteRow		: 'Supprimer les lignes'
		},

		column :
		{
			menu			: 'Colonnes',
			insertBefore	: 'Insérer une colonne avant',
			insertAfter		: 'Insérer une colonne après',
			deleteColumn	: 'Supprimer les colonnes'
		}
	},

	// Button Dialog.
	button :
	{
		title		: 'Propriétés du bouton',
		text		: 'Texte (Value)',
		type		: 'Type',
		typeBtn		: 'Bouton',
		typeSbm		: 'Validation (submit)',
		typeRst		: 'Remise à zéro'
	},

	// Checkbox and Radio Button Dialogs.
	checkboxAndRadio :
	{
		checkboxTitle : 'Propriétés de la case à cocher',
		radioTitle	: 'Propriétés du bouton Radio',
		value		: 'Valeur',
		selected	: 'Sélectionné'
	},

	// Form Dialog.
	form :
	{
		title		: 'Propriétés du formulaire',
		menu		: 'Propriétés du formulaire',
		action		: 'Action',
		method		: 'Méthode',
		encoding	: 'Encodage'
	},

	// Select Field Dialog.
	select :
	{
		title		: 'Propriétés du menu déroulant',
		selectInfo	: 'Informations sur le menu déroulant',
		opAvail		: 'Options disponibles',
		value		: 'Valeur',
		size		: 'Taille',
		lines		: 'Lignes',
		chkMulti	: 'Permettre les sélections multiples',
		opText		: 'Texte',
		opValue		: 'Valeur',
		btnAdd		: 'Ajouter',
		btnModify	: 'Modifier',
		btnUp		: 'Haut',
		btnDown		: 'Bas',
		btnSetValue : 'Définir comme valeur sélectionnée',
		btnDelete	: 'Supprimer'
	},

	// Textarea Dialog.
	textarea :
	{
		title		: 'Propriétés de la zone de texte',
		cols		: 'Colonnes',
		rows		: 'Lignes'
	},

	// Text Field Dialog.
	textfield :
	{
		title		: 'Propriétés du champ texte',
		name		: 'Nom',
		value		: 'Valeur',
		charWidth	: 'Taille des caractères',
		maxChars	: 'Nombre maximum de caractères',
		type		: 'Type',
		typeText	: 'Texte',
		typePass	: 'Mot de passe'
	},

	// Hidden Field Dialog.
	hidden :
	{
		title	: 'Propriétés du champ caché',
		name	: 'Nom',
		value	: 'Valeur'
	},

	// Image Dialog.
	image :
	{
		title		: 'Propriétés de l\'image',
		titleButton	: 'Propriétés du bouton image',
		menu		: 'Propriétés de l\'image',
		infoTab		: 'Informations sur l\'image',
		btnUpload	: 'Envoyer sur le serveur',
		upload		: 'Envoyer',
		alt			: 'Texte de remplacement',
		lockRatio	: 'Conserver les proportions',
		resetSize	: 'Taille d\'origine',
		border		: 'Bordure',
		hSpace		: 'Espacement horizontal',
		vSpace		: 'Espacement vertical',
		alertUrl	: 'Veuillez entrer l\'adresse de l\'image',
		linkTab		: 'Lien',
		button2Img	: 'Voulez-vous transformer le bouton image sélectionné en simple image?',
		img2Button	: 'Voulez-vous transformer l\'image en bouton image?',
		urlMissing	: 'L\'adresse source de l\'image est manquante.',
		validateBorder	: 'Bordure doit être un entier.',
		validateHSpace	: 'HSpace doit être un entier.',
		validateVSpace	: 'VSpace doit être un entier.'
	},

	// Flash Dialog
	flash :
	{
		properties		: 'Propriétés du Flash',
		propertiesTab	: 'Propriétés',
		title			: 'Propriétés du Flash',
		chkPlay			: 'Jouer automatiquement',
		chkLoop			: 'Boucle',
		chkMenu			: 'Activer le menu Flash',
		chkFull			: 'Permettre le plein écran',
 		scale			: 'Echelle',
		scaleAll		: 'Afficher tout',
		scaleNoBorder	: 'Pas de bordure',
		scaleFit		: 'Taille d\'origine',
		access			: 'Accès aux scripts',
		accessAlways	: 'Toujours',
		accessSameDomain: 'Même domaine',
		accessNever		: 'Jamais',
		alignAbsBottom	: 'Bas absolu',
		alignAbsMiddle	: 'Milieu absolu',
		alignBaseline	: 'Bas du texte',
		alignTextTop	: 'Haut du texte',
		quality			: 'Qualité',
		qualityBest		: 'Meilleure',
		qualityHigh		: 'Haute',
		qualityAutoHigh	: 'Haute Auto',
		qualityMedium	: 'Moyenne',
		qualityAutoLow	: 'Basse Auto',
		qualityLow		: 'Basse',
		windowModeWindow: 'Fenêtre',
		windowModeOpaque: 'Opaque',
		windowModeTransparent : 'Transparent',
		windowMode		: 'Mode fenêtre',
		flashvars		: 'Variables du Flash',
		bgcolor			: 'Couleur d\'arrière-plan',
		hSpace			: 'Espacement horizontal',
		vSpace			: 'Espacement vertical',
		validateSrc		: 'L\'adresse ne doit pas être vide.',
		validateHSpace	: 'L\'espacement horizontal doit être un nombre.',
		validateVSpace	: 'L\'espacement vertical doit être un nombre.'
	},

	// Speller Pages Dialog
	spellCheck :
	{
		toolbar			: 'Vérifier l\'orthographe',
		title			: 'Vérifier l\'orthographe',
		notAvailable	: 'Désolé, le service est indisponible actuellement.',
		errorLoading	: 'Erreur du chargement du service depuis l\'hôte : %s.',
		notInDic		: 'N\'existe pas dans le dictionnaire.',
		changeTo		: 'Modifier pour',
		btnIgnore		: 'Ignorer',
		btnIgnoreAll	: 'Ignorer tout',
		btnReplace		: 'Remplacer',
		btnReplaceAll	: 'Remplacer tout',
		btnUndo			: 'Annuler',
		noSuggestions	: '- Aucune suggestion -',
		progress		: 'Vérification de l\'orthographe en cours...',
		noMispell		: 'Vérification de l\'orthographe terminée : aucune erreur trouvée.',
		noChanges		: 'Vérification de l\'orthographe terminée : Aucun mot corrigé.',
		oneChange		: 'Vérification de l\'orthographe terminée : Un seul mot corrigé.',
		manyChanges		: 'Vérification de l\'orthographe terminée : %1 mots corrigés.',
		ieSpellDownload	: 'La vérification d\'orthographe n\'est pas installée. Voulez-vous la télécharger maintenant?'
	},

	smiley :
	{
		toolbar	: 'Émoticones',
		title	: 'Insérer un émoticone',
		options : 'Options des émoticones'
	},

	elementsPath :
	{
		eleLabel : 'Elements path',
		eleTitle : '%1 éléments'
	},

	numberedlist	: 'Insérer/Supprimer la liste numérotée',
	bulletedlist	: 'Insérer/Supprimer la liste à puces',
	indent			: 'Augmenter le retrait (tabulation)',
	outdent			: 'Diminuer le retrait (tabulation)',

	justify :
	{
		left	: 'Aligner à gauche',
		center	: 'Centrer',
		right	: 'Aligner à droite',
		block	: 'Justifier'
	},

	blockquote : 'Citation',

	clipboard :
	{
		title		: 'Coller',
		cutError	: 'Les paramètres de sécurité de votre navigateur ne permettent pas à l\'éditeur d\'exécuter automatiquement l\'opération "couper". Veuillez utiliser le raccourci clavier (Ctrl/Cmd+X).',
		copyError	: 'Les paramètres de sécurité de votre navigateur ne permettent pas à l\'éditeur d\'exécuter automatiquement des opérations de copie. Veuillez utiliser le raccourci clavier (Ctrl/Cmd+C).',
		pasteMsg	: 'Veuillez coller le texte dans la zone suivante en utilisant le raccourci clavier (<strong>Ctrl/Cmd+V</strong>) et cliquez sur OK.',
		securityMsg	: 'A cause des paramètres de sécurité de votre navigateur, l\'éditeur n\'est pas en mesure d\'accéder directement à vos données contenues dans le presse-papier. Vous devriez réessayer de coller les données dans la fenêtre.',
		pasteArea	: 'Coller la zone'
	},

	pastefromword :
	{
		confirmCleanup	: 'Le texte à coller semble provenir de Word. Désirez-vous le nettoyer avant de coller?',
		toolbar			: 'Coller depuis Word',
		title			: 'Coller depuis Word',
		error			: 'Il n\'a pas été possible de nettoyer les données collées à la suite d\'une erreur interne.'
	},

	pasteText :
	{
		button	: 'Coller comme texte sans mise en forme',
		title	: 'Coller comme texte sans mise en forme'
	},

	templates :
	{
		button			: 'Modèles',
		title			: 'Contenu des modèles',
		options : 'Options des modèles',
		insertOption	: 'Remplacer le contenu actuel',
		selectPromptMsg	: 'Veuillez sélectionner le modèle pour l\'ouvrir dans l\'éditeur',
		emptyListMsg	: '(Aucun modèle disponible)'
	},

	showBlocks : 'Afficher les blocs',

	stylesCombo :
	{
		label		: 'Styles',
		panelTitle	: 'Styles de mise en page',
		panelTitle1	: 'Styles de blocs',
		panelTitle2	: 'Styles en ligne',
		panelTitle3	: 'Styles d\'objet'
	},

	format :
	{
		label		: 'Format',
		panelTitle	: 'Format de paragraphe',

		tag_p		: 'Normal',
		tag_pre		: 'Formaté',
		tag_address	: 'Adresse',
		tag_h1		: 'Titre 1',
		tag_h2		: 'Titre 2',
		tag_h3		: 'Titre 3',
		tag_h4		: 'Titre 4',
		tag_h5		: 'Titre 5',
		tag_h6		: 'Titre 6',
		tag_div		: 'Normal (DIV)'
	},

	div :
	{
		title				: 'Créer un container DIV',
		toolbar				: 'Créer un container DIV',
		cssClassInputLabel	: 'Classe CSS',
		styleSelectLabel	: 'Style',
		IdInputLabel		: 'Id',
		languageCodeInputLabel	: 'Code de langue',
		inlineStyleInputLabel	: 'Style en ligne',
		advisoryTitleInputLabel	: 'Advisory Title',
		langDirLabel		: 'Sens d\'écriture',
		langDirLTRLabel		: 'Gauche à droite (LTR)',
		langDirRTLLabel		: 'Droite à gauche (RTL)',
		edit				: 'Éditer la DIV',
		remove				: 'Enlever la DIV'
  	},

	iframe :
	{
		title		: 'Propriétés de la IFrame',
		toolbar		: 'IFrame',
		noUrl		: 'Veuillez entrer l\'adresse du lien de la IFrame',
		scrolling	: 'Permettre à la barre de défilement',
		border		: 'Afficher une bordure de la IFrame'
	},

	font :
	{
		label		: 'Police',
		voiceLabel	: 'Police',
		panelTitle	: 'Style de police'
	},

	fontSize :
	{
		label		: 'Taille',
		voiceLabel	: 'Taille de police',
		panelTitle	: 'Taille de police'
	},

	colorButton :
	{
		textColorTitle	: 'Couleur de texte',
		bgColorTitle	: 'Couleur d\'arrière plan',
		panelTitle		: 'Couleurs',
		auto			: 'Automatique',
		more			: 'Plus de couleurs...'
	},

	colors :
	{
		'000' : 'Noir',
		'800000' : 'Marron',
		'8B4513' : 'Brun moyen',
		'2F4F4F' : 'Vert sombre',
		'008080' : 'Canard',
		'000080' : 'Bleu marine',
		'4B0082' : 'Indigo',
		'696969' : 'Gris foncé',
		'B22222' : 'Rouge brique',
		'A52A2A' : 'Brun',
		'DAA520' : 'Or terni',
		'006400' : 'Vert foncé',
		'40E0D0' : 'Turquoise',
		'0000CD' : 'Bleu royal',
		'800080' : 'Pourpre',
		'808080' : 'Gris',
		'F00' : 'Rouge',
		'FF8C00' : 'Orange foncé',
		'FFD700' : 'Or',
		'008000' : 'Vert',
		'0FF' : 'Cyan',
		'00F' : 'Bleu',
		'EE82EE' : 'Violet',
		'A9A9A9' : 'Gris moyen',
		'FFA07A' : 'Saumon',
		'FFA500' : 'Orange',
		'FFFF00' : 'Jaune',
		'00FF00' : 'Lime',
		'AFEEEE' : 'Turquoise clair',
		'ADD8E6' : 'Bleu clair',
		'DDA0DD' : 'Prune',
		'D3D3D3' : 'Gris clair',
		'FFF0F5' : 'Fard Lavande',
		'FAEBD7' : 'Blanc antique',
		'FFFFE0' : 'Jaune clair',
		'F0FFF0' : 'Honeydew',
		'F0FFFF' : 'Azur',
		'F0F8FF' : 'Bleu Alice',
		'E6E6FA' : 'Lavande',
		'FFF' : 'Blanc'
	},

	scayt :
	{
		title			: 'Vérification de l\'Orthographe en Cours de Frappe (SCAYT)',
		opera_title		: 'Non supporté par Opera',
		enable			: 'Activer SCAYT',
		disable			: 'Désactiver SCAYT',
		about			: 'A propos de SCAYT',
		toggle			: 'Activer/Désactiver SCAYT',
		options			: 'Options',
		langs			: 'Langues',
		moreSuggestions	: 'Plus de suggestions',
		ignore			: 'Ignorer',
		ignoreAll		: 'Ignorer Tout',
		addWord			: 'Ajouter le mot',
		emptyDic		: 'Le nom du dictionnaire ne devrait pas être vide.',
		noSuggestions	: 'Aucune suggestion',
		optionsTab		: 'Options',
		allCaps			: 'Ignorer les mots entièrement en majuscules',
		ignoreDomainNames : 'Ignorer les noms de domaines',
		mixedCase		: 'Ignorer les mots à casse multiple',
		mixedWithDigits	: 'Ignorer les mots contenant des chiffres',

		languagesTab	: 'Langues',

		dictionariesTab	: 'Dictionnaires',
		dic_field_name	: 'Nom du dictionnaire',
		dic_create		: 'Créer',
		dic_restore		: 'Restaurer',
		dic_delete		: 'Effacer',
		dic_rename		: 'Renommer',
		dic_info		: 'Initialement, le dictionnaire de l\'utilisateur est stocké dans un cookie. Cependant, les cookies sont limités en taille. Quand le dictionnaire atteint une taille qu\'il n\'est plus possible de stocker dans un cookie, il peut alors être stocké sur nos serveurs. Afin de stocker votre dictionnaire personnel sur nos serveurs, vous devez spécifier un nom pour ce dictionnaire. Si vous avez déjà un dictionnaire stocké, merci de taper son nom puis cliquer sur Restaurer pour le récupérer.',

		aboutTab		: 'À propos de'
	},

	about :
	{
		title		: 'À propos de CKEditor',
		dlgTitle	: 'À propos de CKEditor',
		help	: 'Consulter $1 pour l\'aide.',
		userGuide : 'Guide de l\'utilisateur CKEditor en anglais',
		moreInfo	: 'Pour les informations de licence, veuillez visiter notre site web:',
		copy		: 'Copyright &copy; $1. Tous droits réservés.'
	},

	maximize : 'Agrandir',
	minimize : 'Minimiser',

	fakeobjects :
	{
		anchor		: 'Ancre',
		flash		: 'Animation Flash',
		iframe		: 'IFrame',
		hiddenfield	: 'Champ caché',
		unknown		: 'Objet inconnu'
	},

	resize : 'Déplacer pour modifier la taille',

	colordialog :
	{
		title		: 'Choisir une couleur',
		options	:	'Option des couleurs',
		highlight	: 'Détails',
		selected	: 'Couleur choisie',
		clear		: 'Effacer'
	},

	toolbarCollapse	: 'Enrouler la barre d\'outils',
	toolbarExpand	: 'Dérouler la barre d\'outils',

	toolbarGroups :
	{
		document : 'Document',
		clipboard : 'Presse-papier/Défaire',
		editing : 'Editer',
		forms : 'Formulaires',
		basicstyles : 'Styles de base',
		paragraph : 'Paragraphe',
		links : 'Liens',
		insert : 'Insérer',
		styles : 'Styles',
		colors : 'Couleurs',
		tools : 'Outils'
	},

	bidi :
	{
		ltr : 'Direction du texte de la gauche vers la droite',
		rtl : 'Direction du texte de la droite vers la gauche'
	},

	docprops :
	{
		label : 'Propriétés du document',
		title : 'Propriétés du document',
		design : 'Design',
		meta : 'Métadonnées',
		chooseColor : 'Choisissez',
		other : '<autre>',
		docTitle :	'Titre de la page',
		charset : 	'Encodage de caractère',
		charsetOther : 'Autre encodage de caractère',
		charsetASCII : 'ASCII',
		charsetCE : 'Europe Centrale',
		charsetCT : 'Chinois Traditionnel (Big5)',
		charsetCR : 'Cyrillique',
		charsetGR : 'Grec',
		charsetJP : 'Japonais',
		charsetKR : 'Coréen',
		charsetTR : 'Turc',
		charsetUN : 'Unicode (UTF-8)',
		charsetWE : 'Occidental',
		docType : 'Type de document',
		docTypeOther : 'Autre type de document',
		xhtmlDec : 'Inclure les déclarations XHTML',
		bgColor : 'Couleur de fond',
		bgImage : 'Image de fond',
		bgFixed : 'Image fixe sans défilement',
		txtColor : 'Couleur de texte',
		margin : 'Marges',
		marginTop : 'Haut',
		marginLeft : 'Gauche',
		marginRight : 'Droite',
		marginBottom : 'Bas',
		metaKeywords : 'Mots-clés (séparés par des virgules)',
		metaDescription : 'Description',
		metaAuthor : 'Auteur',
		metaCopyright : 'Copyright',
		previewHtml : '<p>Ceci est un <strong>texte d\'exemple</strong>. Vous utilisez <a href="javascript:void(0)">CKEditor</a>.</p>'
	}
};
