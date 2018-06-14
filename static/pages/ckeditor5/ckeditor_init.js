ClassicEditor
    .create( document.querySelector( '#editor' ), {
            // removePlugins: [ 'Heading', 'Link' ],
            // plugins: [ Essentials, Paragraph, Bold, Italic, Alignment ],
            // toolbar: [ 'heading', '|', 'bold', 'italic', 'link', 'bulletedList', 'numberedList', 'blockQuote', ],
            // heading: {options: [{ modelElement: 'paragraph', title: 'Paragraph', class: 'ck-heading_paragraph' },{ modelElement: 'heading1', viewElement: 'h1', title: 'Heading 1', class: 'ck-heading_heading1' },{ modelElement: 'heading2', viewElement: 'h2', title: 'Heading 2', class: 'ck-heading_heading2' },]},
            
    } )
    .then( editor => {
        console.log( editor );
        // editor.setData( '<p>Какой-то текст.</p>' );
    } )
    .catch( error => {
        console.error( error );
    } );
