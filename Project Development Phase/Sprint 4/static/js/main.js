$(document).ready(function () {
  // Init
  $(".loader").hide();
  $("#result").hide();

  // Predict
  $("#btn-predict").click(function () {
    // Show loading animation
    $(this).hide();
    $(".loader").show();

    // Make prediction by calling api /predict
    $.ajax({
      type: "POST",
      url: "/predict",
      data: form_data,
      contentType: false,
      cache: false,
      processData: false,
      async: true,
      success: function (data) {
        // Get and display the result
        $(".loader").hide();
        $("#result").fadeIn(600);
        $("#result").text(" Result:  " + data);
        console.log("Success!");
      },
    });
  });
});
