function generateApple() {
    console.log("generating new image");
    $.ajax({
                    type: "POST", // Method type GET/POST           
                    url: "../php/runpython.php", //Ajax Action url
                    data: {},

                    // Before call ajax you can do activity like please wait message
                    beforeSend: function(xhr){
                        resp.html("Please wait...");
                    },

                    //Will call if method not exists or any error inside php file
                    error: function(qXHR, textStatus, errorThrow){
                        resp.html("There are an error");
                    },

                    success: function(data, textStatus, jqXHR){
                        resp.html(data);
                    }
                });
}