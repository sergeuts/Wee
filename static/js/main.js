document.addEventListener('DOMContentLoaded', function() {
    let elems = document.querySelectorAll('.carousel');
    let instances = M.Carousel.init(elems, {
        duration: 200,
        disr: 0,
        padding: 20,
        numVisible: 3,
        fullWidth: true,
        indicators: true,
    });
})

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.tooltipped');
    var instances = M.Tooltip.init(elems, options);
});