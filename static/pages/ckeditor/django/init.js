/**
 * @license Copyright (c) 2003-2018, CKSource - Sergey Kovalchuk. All rights reserved.
 */

$(document).ready(function () {
    // You can specify your own selector. Еxample: '#id_content' instead of 'textarea'
    $('textarea').ckeditor({customConfig: 'django/config.js', });
});
