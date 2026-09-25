if (!customElements.get('zx-tabs')) {
  customElements.define(
    'zx-tabs',
    class ZxTabs extends HTMLElement {
      connectedCallback() {
        this.tabs = Array.from(this.querySelectorAll(':scope > .zx-tabs__list > [role="tab"]'));
        if (!this.tabs.length) return;
        this.tabs.forEach((tab, index) => {
          tab.addEventListener('click', () => this.select(index, false));
          tab.addEventListener('keydown', (event) => this.onKeydown(event, index));
        });
        this.addEventListener('shopify:block:select', (event) => {
          const index = this.tabs.findIndex((tab) => tab.contains(event.target) || tab === event.target);
          if (index > -1) this.select(index, false);
        });
      }

      onKeydown(event, index) {
        const last = this.tabs.length - 1;
        const keys = { ArrowRight: index === last ? 0 : index + 1, ArrowLeft: index === 0 ? last : index - 1, Home: 0, End: last };
        if (!(event.key in keys)) return;
        event.preventDefault();
        this.select(keys[event.key], true);
      }

      select(index, focus) {
        this.tabs.forEach((tab, i) => {
          const selected = i === index;
          const panel = this.querySelector(`#${tab.getAttribute('aria-controls')}`);
          tab.setAttribute('aria-selected', selected ? 'true' : 'false');
          tab.tabIndex = selected ? 0 : -1;
          if (panel) panel.hidden = !selected;
        });
        if (focus) this.tabs[index].focus();
      }
    }
  );
}
