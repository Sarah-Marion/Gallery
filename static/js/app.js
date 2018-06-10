$(document).ready(function() {
    //*************************
    $(window).scroll(function() {
      var sticky = $('#wrap').offset().top;
  
      if ($(window).scrollTop() >= sticky) {
        $(".sticky-header").css("display", "block")
        $(".scroll-category").css("position", "fixed")
        $(".scroll-category").css("top", "9%")
        $(".scroll-category").css("margin-bottom", "2%")
        $(".scroll-category").css("background-color", "#037bb5")
        $(".scroll-category button").css("background", "#dbdbdb")
        $(".scroll-category button").css("color", "#037bb5")
      } else {
        $(".sticky-header").css("display", "none");
        $("header").css("display", "block")
        $('.scroll-category').css("position", "inherit")
        $(".scroll-category").css("background-color", "inherit")
      }
  
    })
  
    //*****************************
    $('.category-button').click(function(event) {
      event.preventDefault()
      var btn_value = $(this).text()
  
      $.ajax({
        'url': 'category/',
        'type': 'GET',
        'data': {
          category_name: btn_value
        },
        'success': function(resp) {
          $('.container-fluid').empty()
          $('.container-fluid').html(resp)
        },
  
      })
    })
    //*************************
    $('option').click(function() {
      if ($(this).is(':selected')) {
        option_value = $(this).text()
        $.ajax({
          'url': 'location/',
          'type': 'GET',
          'data': {
            location_name: option_value
          },
          'success': function(resp) {
            $('.container-fluid').empty()
            $('.container-fluid').html(resp)
          },
  
        })
      }
  
    })
  
    //*************************
  
    $('.myImg').click(function() {
      $('#modal-img').css('display', 'block')
      $(".img-m").attr('src', $(this).attr('src'));
      var img_name = $(this).attr("alt");
      $("#caption").html("Image Name:" + img_name);
    })
  
    $('button#details').click(function() {
      $('#modal-details').css('display', 'block')
      img_d = $(this).data("description");
      loc_d = $(this).data("location");
      cat_d = $(this).data("category");
      cre_d = $(this).data("created");
      $(".one").text(img_d);
      $(".two").text(loc_d);
      $(".three").text(cat_d);
      $(".four").text(cre_d);
    })
  
    $(".close").click(function() {
      $('#modal-img').css('display', 'none')
      $('#modal-details').css('display', 'none')
    })
  
    //*******************************
  
    $('button#btn-copy').each(function() {
      var $this = $(this);
      $this.click(function() {
        var copy = function(e) {
          e.preventDefault();
  
          var text = $this.data('info')
  
          if (e.clipboardData) {
            e.clipboardData.setData('text/plain', text);
          } else if (window.clipboardData) {
            window.clipboardData.setData('Text', text);
          }
        }
  
        window.addEventListener('copy', copy);
        document.execCommand('copy');
        window.removeEventListener('copy', copy);
  
        $this.find("#myPopup").addClass("show");
        $this.find("#myPopup").delay(2000).fadeOut();
        setTimeout(function() {
          $this.find("#myPopup").removeClass("show");
        }, 2001)
      })
    })
    //******************************
  
    $(".collapse").on('shown.bs.collapse', function() {
      $(".scroll-category").css("top", "40%")
    })
    $(".collapse").on('hide.bs.collapse', function() {
      $(".scroll-category").css("top", "9%")
    });
  
    $('.img-Img').each(function() {
      $(this).hover(function() {
        $(this).find('#btn-copy').toggle()
        $(this).find('#see-me').toggle()
        $(this).find('#details').toggle()
      })
    })
  
  })