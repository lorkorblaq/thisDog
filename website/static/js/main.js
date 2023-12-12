// sidebar.js
$("documents").ready(function () {
    $(".sidebar-btn").click(function () {
        $(".sidebar").toggleClass("visible");
    });

    function toggleSidebar() {
        const sidebar = document.querySelector('.sidebar');
        sidebar.classList.toggle('open');
        sidebar.classList.toggle('close');
        }

    function closeSidebar() {
        const sidebar = document.querySelector('.sidebar');
        sidebar.classList.add('close');
        sidebar.classList.remove('open');
        }

    $(".imgh").click(func1);
    function func1(){
        $("img").animate({
            right:'150px',
            opacity: '1',
            height: '89px',
            width: '50px'
        },2000)   
        // $("img").slideToggle(2000);
    }
});


//fadein; fadeout; fadeToggle; hide; show; toggle; slideUp; slideIn; slideToggle
