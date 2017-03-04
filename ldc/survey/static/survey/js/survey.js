(function($){
    $(document).ready(function(){

        function handleDrop(event, ui){
            ui.draggable.removeClass('ui-draggable');
            ui.draggable.removeAttr("style")
            $(this).children("table").append(ui.draggable);
        }

        $(".talent").draggable({
            cursor: "move",
            snap: ".grid-box",
            snapMode: "inner",
            revert: "invalid"
        });
        $(".grid-box").droppable({
            drop: handleDrop
        });

        $(".tooltip").tooltip({
            position: { my: "bottom", at: "top+30"}
        });

        $("#submit-button").click(function(evt){
            // Collect from the boxes into the inputs
            $.each(['learn','mentor','inapinch','forgetit'],function(i,val){
                var talents = [];
                $("#" + val).find(".talent").each(function(){
                    talents.push($(this).attr("id"));
                });
                $("input[name='" + val + "']").val(talents.join());
                console.log(talents);
            });
        });
    });
})(jQuery)
