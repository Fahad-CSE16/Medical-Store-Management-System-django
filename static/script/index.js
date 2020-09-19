// JavaScript Document
$(document).ready(function() {

   /*$("#masque").hide();

   $("a#afficher").click(function() {
      $("#masque").show("fast");
      return false;
   });*/
  // console.log($(window).height());
   //$("#landing-convention").css({"padding-top":$(window).height()+"px"});

	/*$('#landing-convention').prepend(paper);*/
	//$("#box").scroll(function(){});
	//effet par defaut

	$('.tooltip').tooltipster();

	// COMMON !!
	$(".scale-effect,.bouton-rounded").hover(function(element){
  			//alert(element);
  			$(this).css({'transform':'scale(1.05)','box-shadow': '0px 0px 12px #555'});
  		},function(){
 			$(this).css({'transform':'scale(1)','box-shadow': '0px 0px 0px #555'});
	});

	$(".scale-effect-no-shadow").hover(function(element){
  			//alert(element);
  			$(this).css({'transform':'scale(1.05)'});
  		},function(){
 			$(this).css({'transform':'scale(1)'});
	});
	
		//Effet lien par defaut
	$("a").hover(function(element){
  			//alert(element);
  			$(this).animate({"opacity":0.7},50);
  		},function(){
 			$(this).animate({"opacity":1},50);
	});

	//tips effect
	$(".tips").each(function(element){
		var link = $(this).find("a:first");
		var toolTips_content = $(this).find(".tips-content:first");

		link.tooltipster({
			content: '<div class="tips-content">' + toolTips_content.html() + '</div>',
			theme: '.tooltipster-shadow',
			position: 'bottom',
			offsetY: 3,
			speed:200,
			animation:'grow'
		});
		toolTips_content.css({"display":"none"});
	});

	//Gestion actus
	var openActu = function () {
		 var init_position = $(window).scrollTop()+$(window).height();
		 var target_position = $(window).scrollTop();
		 public_target_actu_position = target_position;
		  $('#actualite').css({"top":init_position+"px","display":"block","overflow":"auto","height":"100%"});
		  /*$('html, body').animate({
            	scrollTop: 0
       	 	});*/

			$('#actualite #actu-part1,#actu-main').css({"margin-top":200,"margin-bottom":200,})
			$('#actualite #actu-part1,#actu-main').animate({"margin-top":0,"margin-bottom":0},1200);

       	    $('#actualite').animate({
            	"top": target_position
       	 	},750);
			$('#landing-convention,#landing-intro,#master-menu,#main-content').animate({
            	"opacity": 0
       	 	},1500);
       	 	$("#actualite-footer").slideUp(250);

       	 	$("html,body").css({"overflow":"hidden","height":"100%"});

	};

	var closeActu = function () {
		 var target_position = $(window).scrollTop()+$(window).height();
		/* $('html, body').animate({
            	scrollTop: 0
       	 	});*/
       	  // $('#actualite').slideDown(1500);
       	     $('#actualite').animate({
            	"top": target_position
       	 	},750,function() {
    			$(this).css({"display":"none"});
 			 });
			$('#landing-convention,#landing-intro,#master-menu,#main-content').animate({
            	"opacity": 1
       	 	},1500);

			$("#actualite-footer").slideDown(250);

			$("html,body").css({"overflow":"auto","height":"auto"});
       	  //$('#actualite').slideUp(500);
	};

//example
    
//Gestion actus
	var openActu1 = function () {
		 var init_position = $(window).scrollTop()+$(window).height();
		 var target_position = $(window).scrollTop();
		 public_target_actu_position = target_position;
		  $('#actualite1').css({"top":init_position+"px","display":"block","overflow":"auto","height":"100%"});
		  /*$('html, body').animate({
            	scrollTop: 0
       	 	});*/

			$('#actualite1 #actu-part2,#actu-main1').css({"margin-top":200,"margin-bottom":200,})
			$('#actualite1 #actu-part2,#actu-main1').animate({"margin-top":0,"margin-bottom":0},1200);

       	    $('#actualite1').animate({
            	"top": target_position
       	 	},750);
			$('#landing-convention,#landing-intro,#master-menu,#main-content').animate({
            	"opacity": 0
       	 	},1500);
       	 	$("#actualite-footer").slideUp(250);

       	 	$("html,body").css({"overflow":"hidden","height":"100%"});

	};

	var closeActu1 = function () {
		 var target_position = $(window).scrollTop()+$(window).height();
		/* $('html, body').animate({
            	scrollTop: 0
       	 	});*/
       	  // $('#actualite').slideDown(1500);
       	     $('#actualite1').animate({
            	"top": target_position
       	 	},750,function() {
    			$(this).css({"display":"none"});
 			 });
			$('#landing-convention,#landing-intro,#master-menu,#main-content').animate({
            	"opacity": 1
       	 	},1500);

			$("#actualite-footer").slideDown(250);

			$("html,body").css({"overflow":"auto","height":"auto"});
       	  //$('#actualite').slideUp(500);
	};

    
    $('#actualite1').css({"display":"none"});
	$("#open-actu1,.af-box H3").click(openActu1);
	$("#close-actu1").click(closeActu1);

$('#actualite').css({"display":"none"});
	$("#open-actu,.af-box H3").click(openActu);
	$("#close-actu").click(closeActu);


     
  
	//read more escamotable
	$("#actu-main .read-more").click(function(){
		//alert("click detect�!");
		var bt_less = $(this).parent().find(".read-less");
		var actu_block = $(this).parent().parent();
		var more_content = actu_block.find(".actu-more-content");
		var article_texte = actu_block.find(".article-texte");
		var defaut_content = "";
		bt_less.css("display","block");
		$(this).css("display","none");
		actu_block.css({"overflow":"visible","height":"auto"});
		more_content.css('opacity',0).slideDown({duration :800}).animate({opacity:1},{queue:false,duration:'slow'});
		article_texte.slideUp({duration :800}).animate({opacity:0},{queue:false,duration:'slow'});

	});

	$("#actu-main .read-less").click(function(){
		//alert("click detect�!");
		var bt_more = $(this).parent().find(".read-more");
		var actu_block = $(this).parent().parent();
		var more_content = actu_block.find(".actu-more-content");
		var article_texte = actu_block.find(".article-texte");
		//actu_block.css({"overflow":"visible","height":"auto"});
		bt_more.css("display","block");
		$(this).css("display","none");
		article_texte.slideDown({duration :800}).animate({opacity:1},{queue:false,duration:'slow'});
		more_content.slideUp({duration:800});
	});

	// END COMMON!

    
	//Menu
	/*$("#master-menu nav a.item").hover(function(element){
  			//alert(element);
  			$(this).animate({"background-position-y":0},100);
  		},function(){
 			$(this).animate({"background-position-y":-6},100);
	});*/


	var hauteur_bandeau_actu = 35;
	var hauteur_menu_visible = 55;
	var total_offset = hauteur_bandeau_actu + hauteur_menu_visible;
	var init_menu_posY = 0;
	var scroll_menu_anim = false;

	var initMenu = function (re_init) {
		init_menu_posY = $(window).height() - total_offset;
		if (!re_init) {
			$('#master-menu').css({'top':init_menu_posY+"px"});
			//$('body').scrollTo(0,0);
			 $('html, body').animate({
            	scrollTop: 0
       	 	});
		}
		if ($('#landing-convention').length > 0 ) scroll_menu_anim = true;
		gestionMenu();
	}


	var gestionMenu = function () {
			var base_height = $(window).height();
  			var scroll_from_top = $(window).scrollTop();
  		if ( scroll_from_top+total_offset >= base_height || !scroll_menu_anim ) {
  			//effet menu
  			$('#logo-img').fadeIn();
  			$('#logo-img').css({'transform':'scale(1)'});
  			$('#content-nav-left').css({'margin-right':'50px'});
            $('#content-nav-right').css({'margin-left':'50px'});
            $('#user-nav').css({'height':'150px','opacity':1});


             //position menu
			$('#master-menu').css({'top':"-40px"});

  		}else {
  			//effet menu
  			$('#logo-img').fadeOut();
  			$('#logo-img').css({'transform':'scale(0)'});
  			$('#content-nav-right').css({'margin-left':'0px'});
            $('#content-nav-left').css({'margin-right':'0px'});
            $('#user-nav ').css({'height':'0px','opacity':0});

             //position menu
			var menu_posY = init_menu_posY - scroll_from_top ;
			$('#master-menu').css({'top':menu_posY+"px"});

  		}
	}
	var effetScrollContent = function () {
		$(".block-content").each(function(){
			//console.log ( $(this).offset().top + "anim");
			if ( ( $(window).scrollTop()  < $(this).offset().top + $(this).height() - 150) && $(window).scrollTop() + $(window).height() > $(this).offset().top +100 ) { //$(this).height()+ $(this).offset().top-150  > $(window).scrollTop()

				$(this).css({'transform':'scale(1,1)','opacity':1});
			}else {
				$(this).css({'transform':'scale(0.5,1)','opacity':0});
			}
		});
	}

	initMenu(false);
	$(window).scroll(function(){
		gestionMenu();
		effetScrollContent();

		//test
		//$('#main-content,#landing-convention').animate({"background-position-y":-($(window).scrollTop()*0.5)},{duration:500,queue:false});
		//$('#main-content,#landing-convention').css({"background-position-y":-($(window).scrollTop()*0.5)});
		//$('#main-content,#landing-convention').css({"background-position-y":-($(window).scrollTop()*0.5)});
		$('#main-content,#landing-convention').css("background-position", "center "+ " " + (-$(window).scrollTop()*0.2)+"px");
	});

	$(window).resize(function(){
		initMenu(true);
		gestionMenu();
	});


	//action

	$(".convention-link,#menu-item-139,#menu-item-54").click(function(event) {
  		//alert("Handler for .click() called.");
  		 if ( $("#landing-convention").length > 0 ) event.preventDefault();
  		//$('body').scrollTo("#landing-convention",3000);
  		   $('html, body').animate({
        		scrollTop:$("#landing-convention").offset().top
    		},1200);
	});

	//slide exposants
	if ($("#exposant-slide").length > 0 )
		$("#exposant-slide").milk_simpleSlide({"bt_prev":$("#left-exposant"),"bt_next":$("#right-exposant"),"step":205,"timer":2500}); //ex 291
		//slide partenaire
	if ($("#partenaire-slide").length > 0 )
		$("#partenaire-slide").milk_simpleSlide({"bt_prev":$("#left-partenaire"),"bt_next":$("#right-partenaire"),"step":205,"timer":2500}); //ex 251


	//Effet hover stats type 2
	$(".stats2 li").hover(function(element){
  			//alert(element);
  			$(this).find(".hover").css({'transform':'scale(1.1)','box-shadow': '1px 1px 12px #555','opacity':1});
  		},function(){
 			$(this).find(".hover").css({'transform':'scale(1)','opacity':0});
	}).find('.hover').css({'opacity':0});


	//gestion ancre offset
	var offset = 160; // +/- hauteur menu 160
	if ( $('#landing-convention').length > 0 ) offset = -1
	var hash = window.location.hash;
	if (hash) {
		  $('html, body').animate({
	        scrollTop: $(hash).offset().top - offset
	    }, 1000);
	}

});//fin domready



//$(window).load(function () {
//	var ajustText = function () {
//		$('#infos-texte').css({'letter-spacing':'0px'});
//		var Wdiv = $('#infos').width();
//		var Wtext =$('#infos-texte').width();
//		if(Wtext<Wdiv){
//			var Ltext = $('#infos-texte').html().length;
//			var txtspace = (Math.floor((Wdiv-Wtext)*100/Ltext)/100);
//			$('#infos-texte').css({'letter-spacing':txtspace+'px'}); // on ajuste
//		}
//	};
//	ajustText();
//
//});//fin on load

var milk_ActiveCarousselTwitter = function () {
	//twitter carroussel
	$("#twitter-test,#actu-twitter-feed").jContent({orientation: 'vertical',
		width :560,
		height:130,
        easing: 'easeInOutBack',
        speed: 1000,
        auto: true,
        direction: 'next', //or 'prev'
        pause: 3500,
        pause_on_hover: false
     });
     $(".twitter-link").unbind("click");
};