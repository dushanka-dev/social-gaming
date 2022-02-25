// Allow users to toggle comment section of posts
$(document).ready(function(){
    $(".comment-btn").click(function(){
      $(".comments").toggle().css({"background-color": "#090c18"});
    });
  });