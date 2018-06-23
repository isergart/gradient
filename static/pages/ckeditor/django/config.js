/**
 * @license Copyright (c) 2003-2018, CKSource - Sergey Kovalchuk. All rights reserved.
 */

CKEDITOR.editorConfig = function( config ) {
    // Define changes to default configuration here.
    // For complete reference see:
    // http://docs.ckeditor.com/#!/api/CKEDITOR.config

    config.language = 'ru';
    config.uiColor = 'ffffff';
    // config.height = 200;
    // config.width = 800;
    // config.extraPlugins = 'easyimage';
    // config.cloudServices_tokenUrl = 'http://127.0.0.1:8000/cs-token-endpoint';
    // config.cloudServices_uploadUrl = 'http://127.0.0.1:8000/media/uploads/';
    config.extraPlugins = 'autogrow,templates,showblocks';
    config.autoGrow_minHeight = 250;
    config.autoGrow_maxHeight = 1000;
    config.toolbarGroups = [
        { name: 'styles', groups: [ 'styles', 'templates', 'showblocks', ] },
		{ name: 'basicstyles', groups: [ 'basicstyles', 'cleanup' ] },
		{ name: 'paragraph', groups: [ 'list', 'indent', 'blocks', 'align', 'bidi', 'paragraph' ] },
		{ name: 'clipboard', groups: [ 'clipboard', 'undo' ] },
		{ name: 'editing', groups: [ 'find', 'selection', 'spellchecker', 'editing' ] },
		{ name: 'links', groups: [ 'links' ] },
		{ name: 'insert', groups: [ 'insert' ] },
		{ name: 'forms', groups: [ 'forms' ] },
		{ name: 'tools', groups: [ 'tools' ] },
		{ name: 'document', groups: [ 'mode', 'document', 'doctools' ] },
		{ name: 'others', groups: [ 'others' ] },
		{ name: 'colors', groups: [ 'colors' ] },
		{ name: 'about', groups: [ 'about' ] }
    ];

    // Remove some buttons provided by the standard plugins, which are
	// not needed in the Standard(s) toolbar.
    config.removeButtons = 'Underline,Subscript,Superscript,About,Scayt,Table,SpecialChar,Strike,Outdent,Indent,Blockquote,Styles,PasteText,PasteFromWord';

    // Set the most common block elements.
    config.format_tags = 'p;h2;h3';

    // Simplify the dialog windows.
	config.removeDialogTabs = 'image:advanced;link:advanced';

};
