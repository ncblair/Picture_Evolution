$(document).ready(function() {
    $("#generateDefault").click(function() {
        generateApple();
        });
});


function generateApple() {
    console.log("generating new image");
    $resp = $("#generateDefaultLabel");
    $.ajax({
                    type: "POST", // Method type GET/POST           
                    url: "http://nathanblair.me/Picture_Evolution/assets/php/runpython.php", //Ajax Action url
                    data: {},

                    // Before call ajax you can do activity like please wait message
                    beforeSend: function(xhr){
                        $resp.text("Please wait...");
                    },

                    //Will call if method not exists or any error inside php file
                    error: function(qXHR, textStatus, errorThrow){
                        $resp.text("There are an error");
                    },

                    success: function(data, textStatus, jqXHR){
                        console.log(data);
                        $resp.text(data);
                    }
                });
}