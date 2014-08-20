
$(document).ready(function(){

	$("input[type=range]").hover(function(){
		$(this).css("cursor","pointer");
	})

	updateColors();
})


////On Color Slider Change
$("input[type=range]").on("input change",function(){
	var value=$(this).next();
	var colorvalue=Math.round($(this).val())
	value.html(colorvalue);

	updateColors();
});

///Update Color Patches and Gradient
function updateColors(){
	var gradientColors=Array();

	$(".redSlider").each(function(){


		var red=$(this).val();
		var green=$(this).nextAll(".greenSlider").val();
		var blue=$(this).nextAll(".blueSlider").val();

		var colorString="rgb("+red.toString()+","+green.toString()+","+blue.toString()+")";

		///Set Color Patch
		$(this).nextAll(".colorPatch").css("background-color",colorString);

		gradientColors.push(colorString);

	});

		var gradientString="linear-gradient("+gradientColors.join(",")+")";
		////Set Gradient
		$("#gradientBar").css("background",gradientString);

}