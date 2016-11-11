/**
 * Created by iliyaz on 11.10.16.
 */
var obj = document.getElementById('title_text');
var scrolled = obj.getBoundingClientRect().bottom;
var obj_bootom = document.getElementById('hide_menu_title');
var scrolled_bottom = obj_bootom.getBoundingClientRect().bottom;
window.onscroll = function() {
    if (document.body.clientWidth > 801){
        if (scrolled > window.pageYOffset){
            document.getElementById('hide_menu_title').style.top = '0px';
            document.getElementById('hide_menu_title').style.position = 'inherit';
            document.getElementById('slider_top').style.marginTop = '-28px';
            document.getElementById('blog_text').style.top = '60px';
            document.getElementById('blog_service').style.top = '0px';
            document.getElementById('service').style.top = '0px';
            document.getElementById('video').style.top = '0px';
            document.getElementById('service_detail').style.top = '0';
        }else if(scrolled < window.pageYOffset){
            document.getElementById('hide_menu_title').style.position = 'fixed';
            document.getElementById('hide_menu_title').style.top = '-65px';
            document.getElementById('slider_top').style.marginTop = '100px';
            document.getElementById('blog_text').style.top = '60px';
            document.getElementById('blog_service').style.top = '130px';
            document.getElementById('service').style.top = '0px';
            document.getElementById('video').style.top = '170px';
            document.getElementById('service_detail').style.top = '0px';
        }
    }if (document.body.clientWidth > 761){
        if (scrolled > window.pageYOffset){
            document.getElementById('hide_menu_title').style.top = '0px';
            document.getElementById('hide_menu_title').style.position = 'inherit';
            document.getElementById('slider_top').style.marginTop = '-28px';
            document.getElementById('blog_text').style.top = '60px';
            document.getElementById('blog_service').style.top = '0px';
            document.getElementById('service').style.top = '0px';
            document.getElementById('video').style.top = '0px';
            document.getElementById('service_detail').style.top = '0';
        }else if(scrolled < window.pageYOffset){
            document.getElementById('hide_menu_title').style.position = 'fixed';
            document.getElementById('hide_menu_title').style.top = '-65px';
            document.getElementById('slider_top').style.marginTop = '100px';
            document.getElementById('blog_service').style.top = '180px';
            document.getElementById('service').style.top = '0px';
            document.getElementById('video').style.top = '170px';
            document.getElementById('service_detail').style.top = '0px';
        }
    }else if(document.body.clientWidth < 761){
        var obj_bootom = document.getElementById('hide_menu_title');
        var scrolled_bottom = obj_bootom.getBoundingClientRect().bottom;
        document.getElementById('hide_menu_title').style.position = 'fixed';
        document.getElementById('slider_top').style.marginTop='-30px';
        if (scrolled_bottom > window.pageYOffset){
//					document.getElementById('blog_service').style.top = '-75px';
            document.getElementById('slider_top').style.top='0px';
//					document.getElementById('service_detail').style.top = '-45px';
            document.getElementById('block_text').style.marginTop = '-45px';

        }
    }if(document.body.clientWidth < 1000){
        document.getElementById('hide_menu_title').style.position = 'fixed';
        document.getElementById('slider_top').style.marginTop='0px';
        document.getElementById('slider_top').style.marginTop='0px';
    }
};
if(document.body.clientWidth < 761) {
    document.getElementById('hide_menu_title').style.position = 'fixed';
    document.getElementById('slider_top').style.top = '0px';
    document.getElementById('line').style.display = 'none';
    if (scrolled_bottom > window.pageYOffset) {
        document.getElementById('slider_top').style.marginTop = '45px';
    }
}
if(document.body.clientWidth < 1000) {
    document.getElementById('line').style.display = 'none';
}
if(document.body.clientWidth < 980 ){
    document.getElementById('service_detail').style.height = '1200px';
}
if(document.body.clientWidth < 761) {
    document.getElementById('service_detail').style.top = '0px';
    document.getElementById('image_1').style.height = '250px';
    document.getElementById('image_2').style.height = '250px';
    document.getElementById('image_3').style.height = '250px';
    document.getElementById('image_4').style.height = '250px';
    document.getElementById('phone-lang').style.display = 'block';
}else if(document.body.clientWidth > 761){
    document.getElementById('lang-pc').style.display = 'block';
}
if(document.body.clientWidth > 779){
    document.getElementById('map').style.width = '550px';
}
if(document.body.clientWidth < 662 && document.body.clientWidth > 410) {
    document.getElementById('map').style.width = '400px';

}else if(document.body.clientWidth < 412 && document.body.clientWidth > 359){
    document.getElementById('map').style.width = '350px';
}else if(document.body.clientWidth < 359){
    document.getElementById('map').style.width = '300px';
}
if(document.body.clientWidth > 1000 ) {
    document.getElementById('image_1').style.height = '350px';
    document.getElementById('image_2').style.height = '350px';
    document.getElementById('image_3').style.height = '350px';
    document.getElementById('image_4').style.height = '350px';
    document.getElementById('service_detail').style.height = '600px';
    document.getElementById('map').style.width = '100%';
}
if(document.body.clientWidth > 1800) {
    document.getElementById('image_1').style.height = '700px';
    document.getElementById('image_2').style.height = '700px';
    document.getElementById('image_3').style.height = '700px';
    document.getElementById('image_4').style.height = '700px';
    document.getElementById('service_detail').style.height = '600px';
    document.getElementById('map').style.width = '100%';
}
if(document.body.clientWidth > 2000) {
    document.getElementById('image_1').style.height = '800px';
    document.getElementById('image_2').style.height = '800px';
    document.getElementById('image_3').style.height = '800px';
    document.getElementById('image_4').style.height = '800px';
    document.getElementById('image_4').style.height = '800px';
    document.getElementById('service_detail').style.height = '600px';
    document.getElementById('map').style.width = '100%';
}
function isTouchDevice() {
    return true == ("ontouchstart" in window || window.DocumentTouch && document instanceof DocumentTouch);
}
if (isTouchDevice() === true && document.body.clientWidth > 1280) {
    function onHover1()
    {
        document.getElementById('Img1').style.display = 'block';
    }

    function offHover1()
    {
        document.getElementById('Img1').style.display = 'none';
    }
    function onHover2()
    {
        document.getElementById('Img2').style.display = 'block';
    }

    function offHover2()
    {
        document.getElementById('Img2').style.display = 'none';
    }
    function onHover3()
    {
        document.getElementById('Img3').style.display = 'block';
    }

    function offHover3()
    {
        document.getElementById('Img3').style.display = 'none';
    }
}else if(isTouchDevice() === false){
    function onHover1()
    {
        document.getElementById('Img1').style.display = 'block';
    }

    function offHover1()
    {
        document.getElementById('Img1').style.display = 'none';
    }
    function onHover2()
    {
        document.getElementById('Img2').style.display = 'block';
    }

    function offHover2()
    {
        document.getElementById('Img2').style.display = 'none';
    }
    function onHover3()
    {
        document.getElementById('Img3').style.display = 'block';
    }

    function offHover3()
    {
        document.getElementById('Img3').style.display = 'none';
    }
}