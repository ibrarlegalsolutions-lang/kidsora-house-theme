/**
 * <zx-scroller> — progressive-enhancement horizontal scroller used by zx- sections.
 * Markup: a [data-zx-track] scroll-snap list plus optional [data-zx-prev] / [data-zx-next] buttons.
 * Without JS the track still scrolls natively (touch, trackpad, keyboard).
 */
class ZxScroller extends HTMLElement {
  connectedCallback() {
    this.track = this.querySelector('[data-zx-track]');
    this.prev = this.querySelector('[data-zx-prev]');
    this.next = this.querySelector('[data-zx-next]');
    if (!this.track) return;

    this.onPrev = () => this.scrollByPage(-1);
    this.onNext = () => this.scrollByPage(1);
    this.onScroll = () => this.updateButtons();

    this.prev?.addEventListener('click', this.onPrev);
    this.next?.addEventListener('click', this.onNext);
    this.track.addEventListener('scroll', this.onScroll, { passive: true });
    this.resizeObserver = new ResizeObserver(this.onScroll);
    this.resizeObserver.observe(this.track);
    this.updateButtons();
  }

  disconnectedCallback() {
    this.prev?.removeEventListener('click', this.onPrev);
    this.next?.removeEventListener('click', this.onNext);
    this.track?.removeEventListener('scroll', this.onScroll);
    this.resizeObserver?.disconnect();
  }

  scrollByPage(direction) {
    const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const isRtl = getComputedStyle(this.track).direction === 'rtl';
    const distance = this.track.clientWidth * 0.9 * direction * (isRtl ? -1 : 1);
    this.track.scrollBy({ left: distance, behavior: reduce ? 'auto' : 'smooth' });
  }

  updateButtons() {
    const { scrollLeft, scrollWidth, clientWidth } = this.track;
    const position = Math.abs(scrollLeft);
    const overflow = scrollWidth - clientWidth > 2;
    this.toggleAttribute('data-overflowing', overflow);
    if (this.prev) this.prev.disabled = !overflow || position <= 2;
    if (this.next) this.next.disabled = !overflow || position >= scrollWidth - clientWidth - 2;
  }
}

if (!customElements.get('zx-scroller')) customElements.define('zx-scroller', ZxScroller);
