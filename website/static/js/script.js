        // Menunggu halaman sepenuhnya dimuat
        window.onload = function() {
            // Menambahkan kelas animasi pada elemen header
            const headerText = document.querySelector('.header-text');
            if (headerText) {
                headerText.classList.add('fade-in');
            }
        };

        // Lazy loading untuk gambar
        document.addEventListener("DOMContentLoaded", function() {
            const images = document.querySelectorAll('.lazy-img');

            const observerOptions = {
                root: null, // Menggunakan viewport
                rootMargin: '0px',
                threshold: 0.1 // Gambar akan muncul saat 10% elemen terlihat di viewport
            };

            const observer = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        img.classList.add('loaded'); // Tambahkan class 'loaded' untuk animasi
                        observer.unobserve(img); // Stop observing after image has appeared
                    }
                });
            }, observerOptions);

            images.forEach(image => {
                observer.observe(image); // Mulai mengamati setiap gambar
            });
        });


