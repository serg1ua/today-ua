$( document ).ready(function() {
  var tag = "";
  var count = 10;
  var date = timeDate();
  $('#date').html(date.date_time);
  $("#dateShort").html(date.date_time_short);
  $("#year").html(date.year);
  tag = $('#header').text().trim();
  var classAdd = '.nav-link:contains(' + tag + ')';
  $(classAdd).addClass('active');

  $('#hamburger').on('click', function() {
    $('nav').toggleClass('d-none');
  });

  var h4 = document.getElementsByTagName('h4');
  if(h4.length == 1) {
    article(h4[0].innerText);
  }
  var h5 = document.getElementsByTagName('h5');
  if(h5.length < 10) {
    $('button').css('display', 'none');
  }
  $('button').on('click', function() {
    count += 10;
    articles(tag, count);
  });

   //////////  datetime function  //////////
  function timeDate() {
    var time = {};
    var d = new Date();
    var month_num = d.getMonth();
    var day = d.getDate();
    var dayWeek = d.getDay();
    var hours = d.getHours();
    var minutes = d.getMinutes();

    var month = ["Січня", "Лютого", "Березня", "Квітня", "Травня", "Червня",
    "Липня", "Серпня", "Вересня", "Жовтня", "Листопада", "Грудня"];
    var days = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"];
    var daysShort = ["Пн.", "Вт.", "Ср.","Чт.","Пт.","Сб.","Нд."]

    if (day <= 9) day = "0" + day;
    if (hours <= 9) hours = "0" + hours;
    if (minutes <= 9) minutes = "0" + minutes;
    if (dayWeek == 0) dayWeek = 7;

    time.date_time = days[dayWeek - 1] + ", " + day + " " + month[month_num] + " " + d.getFullYear() +
   " p.&nbsp;&nbsp;&nbsp;"  + hours + ":" + minutes;
    time.date_time_short = daysShort[dayWeek - 1] + ", " + day + "/" + month_num + "/" + d.getFullYear() +
   " p.&nbsp;&nbsp;&nbsp;"  + hours + ":" + minutes;
    time.year = d.getFullYear();
    return time;
  }


  function articles(tag, count) {
    $.getJSON("api/articles/" + tag + "&" + count)
      .done(function( json ){
        if(json.length < 10) {
          $('button').attr('disabled', 'true');
          $('button').text('Нема новин');
        }
        var html = '';
        for(var i = 0; i < json.length; i++) {
            var gotoTag = encodeURIComponent(json[i].tag)
            var gotoHeader = encodeURIComponent(json[i].header);
            html += "<div id='media' class='media'><div class='media-left'>" + "<a href=/news/" + gotoTag + '/' + gotoHeader + ">" + "<img class='media-object'" + "src=static/" + json[i].image  + ">" + "</a>" + "</div>" +
            "<div class='media-body'>" + "<time>" + json[i].date + "</time>" + "<a href=/news/" + gotoTag + '/' + gotoHeader + ">" + "<h5 class='media-heading'>" + json[i].header +
            "</h5></a></div></div></div>";
        }
        $("#endblock").before(html);
      })
      .fail(function( jqxhr, textStatus, error ) {
        $('button').attr('disabled', 'true');
        $('button').text('Нема новин');
      });
  }

  function article(header) {
    $.getJSON("api/article/" + decodeURIComponent(header))
      .done(function( json ) {
        $("#content").html(json.text);
      })
      .fail(function( jqxhr, textStatus, error ) {
        $('h4').text("Error, something went wrong");
      });
  }
});