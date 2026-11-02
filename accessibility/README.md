---
last_reviewed: 2026-11-02
---

# Accessibility

[Accessibility regulations](../regulations/README.md#web-accessibility-directive-wad)

## Web Content Accessibility Guidelines (WCAG)

WCAG are a set of guidelines for making the web more accessible. The WCAG standards are versioned, with each version entailing stricter guidelines. The Act on Accessibility to Digital Public Services ("DOS-lagen", see [regulations/README.md](../regulations/README.md#web-accessibility-directive-wad)) requires compliance with WCAG 2.1 level AA [^1].

[How to meet WCAG](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&levels=aaa&hidesidebar=true)

[^1]: [Myndigheten för digital förvaltning](https://www.digg.se/webbriktlinjer/lagar-och-krav/det-har-ar-en-301-549-och-wcag). English page (less information): [Agency for Digital Government](https://www.digg.se/webbriktlinjer/about-webbriktlinjer).

## Setting up your services for compliance

### Manual testing

No automated tools are a replacement for visual inspection. Always review new or changed UI through the lens of
accessibility.

### GitHub Action for web applications: [Pa11y](https://github.com/pa11y/pa11y)

This tool, which can be run in a GitHub Action (see
[the workflow in Pathogens Portal](https://github.com/ScilifelabDataCentre/pathogens-portal/blob/develop/.github/workflows/pa11y_test.yaml)),
performs some automated checks against the specified website or HTML file.

> :warning: If improving the accessibility of an existing application, begin with manual testing and fixing, before
> progressing to this as you will undoubtedly get many initial failures.

### Other useful tools

#### [WAVE](https://wave.webaim.org/)

This tool complements Pa11y and can be used by submitting a URL to their website or using the browser extension.

#### Screen readers

Test the experience of using the application using a screen reader, e.g. [NVDA](https://www.nvaccess.org/download/).

#### Contrast checker

Contrast (or lack thereof) is a cause of many accessibility issues. Tools for explicitly checking this, such as
https://www.siegemedia.com/contrast-ratio, complement WAVE and Pa11y and provide more information on a contrast
ratio given the font size.

### Data Centre/SciLifeLab-specific considerations

We use the [SciLifeLab brand colours](https://www.scilifelab.se/community-pages/resources/visual-identity/) in our services, but we need to keep accessibility in mind. Other services may be bound by the design restrictions of the backing host university or funding
agency.

#### Tips

- If links are Teal and the background is Aqua, there is insufficient contrast.
- Play around with the text colour (e.g. black vs white).
- In addition to checking the ratio number using the tools listed above, zoom out the page as much as possible or take
  physical steps away from the monitor.

## Further reading

- https://inclusive.microsoft.design/
- https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/What_is_accessibility
