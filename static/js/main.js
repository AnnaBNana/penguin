$(document).ready(function() {
  var id,
  loc = location.pathname;

  function parse_filter_value() {
    var filterStr = "filter="
    var filterStart = location.search.indexOf(filterStr) + filterStr.length
    var filterEnd = location.search.indexOf("&")
    var filter = location.search.substring(filterStart, filterEnd)
    var valueStr = "value="
    var valueStart = location.search.indexOf(valueStr) + valueStr.length
    var valueEnd = location.search.indexOf("&", filterEnd + 1)
    var value = location.search.substring(valueStart, valueEnd)
    return [filter, value]
  }

  // HIGHLIGHT ACTIVE SECTION IN NAVBAR
  if (loc.startsWith('/learn/')) {
    $('.learn').addClass('active');
    $(".glasses").css("color", "tomato");
  }
  else if (loc.startsWith('/blog/')) {
    $('.blog').addClass('active');
    $(".blog-icon").css("color", "tomato");
  } else {
    if (loc == "/filter") {
      var filter_value = parse_filter_value()
      var filter = filter_value[0]
      var value = filter_value[1]
      if (filter == "all") {
        $('#all').addClass('highlighted');
      } else {
        $('#' + value).addClass('highlighted');
      }
    }
    if (loc.search('/cart') > -1) {
      $('.cart').addClass('active');
    } else {
      $('.shop').addClass('active');
      $(".pen").css("color", "tomato");
    }
  }

  // MATERIALIZE INITIALIZERS
  $('.modal').modal();
  $('.modal-trigger').click(function(){
    id = $(this).attr('id')
    $('#modal' + id).modal('open');
  });

  $('.closer').click(function(e){
    var modalID = "#" + e.target.parentElement.parentElement.parentElement.id
    $(modalID).modal('close');
  });

  // SETTINGS FOR SLICK SLIDER
  $(".slider-for").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    fade: true,
    asNavFor: ".slider-nav",
    adaptiveHeight: true
  });
  $(".slider-nav").slick({
    variableWidth: true,
    infinite: false,
    centerMode: true,
    asNavFor: ".slider-for",
    lazyLoad: 'ondemand',
    focusOnSelect: true,
    dots: true
  });

  $('.button-collapse').sideNav();

  // highlight selected article in sidebar
  if ($('.article-item').length) {
    var item_id = 0,
    article_id = $("#article").attr("data-id");
    $(".article-item").each(function(){
      item_id = $(this).attr("data-id");
      if (item_id == article_id) {
        $(this).addClass("highlighted");
      }
    });
  };

  // highlight selected blog in sidebar
  if ($('.blog-item').length) {
    var item_id = 0,
    article_id = $("#blog").attr("data-id");
    $(".blog-item").each(function () {
      item_id = $(this).attr("data-id");
      if (item_id == article_id) {
        $(this).addClass("highlighted");
      }
    });
  };

  // display materialize select menus
  $('select').material_select();
  document.querySelectorAll(
    '.select-wrapper'
  ).forEach(
    t => t.addEventListener(
      'click', e => e.stopPropagation()
    )
  );
  $('select[required]').css({
    display: 'inline',
    position: 'absolute',
    float: 'left',
    padding: 0,
    margin: 0,
    border: '1px solid rgba(255,255,255,0)',
    height: 0,
    width: 0,
    top: '2em',
    left: '3em',
    opacity: 0,
    pointerEvents: 'none'
  });
});
