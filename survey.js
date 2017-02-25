(function($){
    $(document).ready(function(){

        function handleDrop(event, ui){
            ui.draggable.removeClass('ui-draggable');
            ui.draggable.removeAttr("style")
            $(this).children("table").append(ui.draggable);
        }

        $(".talent").draggable({
            cursor: 'move',
            snap: '.grid-box',
            snapMode: 'inner',
            revert: "invalid"
        });
        $(".grid-box").droppable({
            drop: handleDrop
        });

        $(".tooltip").tooltip({
            position: { my: "bottom", at: "top+30"}
        });
    });
})(jQuery)
