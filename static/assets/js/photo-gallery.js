// Debounce function to limit the rate of function execution
function debounce(func, wait) {
    let timeout;
    return function (...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(this, args), wait);
    };
}

// Initialize the infinite scrolling carousel
function initInfiniteCarousel(carouselSelector, scrollSpeed) {
    const carousel = document.querySelector(carouselSelector);
    if (!carousel) return;

    const originalItems = Array.from(carousel.querySelectorAll('a'));
    let totalScroll = 0;
    let animationFrameId;
    let singleCycleWidth = 0; // Width of one cycle of original items
    const firstItemMarginLeft = parseFloat(getComputedStyle(originalItems[0]).marginLeft); // Margin-left of the first item
    let isPaused = false; // To keep track of the pause state

    // Function to handle pause on hover for the entire carousel
    function addHoverListeners() {
        carousel.addEventListener('mouseenter', () => {
            isPaused = true; // Pause the scrolling
        });
        carousel.addEventListener('mouseleave', () => {
            isPaused = false; // Resume the scrolling
        });
    }

    // Function to calculate and duplicate items to fill the viewport
    function fillCarousel() {
        const viewportWidth = window.innerWidth; // Update viewport width on resize
        singleCycleWidth = firstItemMarginLeft; // Reset and include margin-left only for the first item

        // Clear existing clones
        carousel.querySelectorAll('.clone').forEach((clone) => clone.remove());

        // Calculate the width of the original items, including margins
        originalItems.forEach((item) => {
            const itemWidth = item.getBoundingClientRect().width + parseFloat(getComputedStyle(item).marginRight);
            singleCycleWidth += itemWidth;
        });

        // Calculate how many duplicates are needed to fill at least twice the viewport width
        const numDuplicates = Math.ceil((viewportWidth * 2) / singleCycleWidth);

        // Create duplicates to fill the carousel
        for (let i = 0; i < numDuplicates; i++) {
            originalItems.forEach((item) => {
                const clone = item.cloneNode(true);
                clone.classList.add('clone');
                carousel.appendChild(clone);
            });
        }
    }

    // Function to handle infinite scrolling animation
    function animateScroll() {
        if (!isPaused) {
            totalScroll += scrollSpeed;

            // Smoothly move items instead of resetting the scroll position
            if (totalScroll >= singleCycleWidth) {
                const firstOriginalItem = carousel.querySelector('a');
                const clone = firstOriginalItem.cloneNode(true);
                clone.classList.add('clone');
                carousel.appendChild(clone);
                firstOriginalItem.remove();
                totalScroll -= singleCycleWidth;
            }

            carousel.style.transform = `translateX(-${totalScroll}px)`;
        }

        animationFrameId = requestAnimationFrame(animateScroll);
    }

    // Function to reset the animation on viewport resize
    const resetAnimationOnResize = debounce(() => {
        cancelAnimationFrame(animationFrameId); // Cancel the current animation
        fillCarousel(); // Recalculate the dimensions and refill the carousel
        totalScroll = 0; // Reset scroll position
        animateScroll(); // Restart the animation
    }, 250);

    // Initialize the carousel fill, start animation, and add hover listeners
    fillCarousel();
    animateScroll();
    addHoverListeners(); // Attach hover listeners to the entire carousel

    // Refill carousel on window resize and restart animation
    window.addEventListener('resize', resetAnimationOnResize);
}

// Initialize the infinite carousel
initInfiniteCarousel('#photo-gallery', 1); // Adjust scrollSpeed to your liking