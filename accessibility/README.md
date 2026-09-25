# Accessibility

The European Accessibility Act (EAA) came into law in 2025. In short, businesses and governmental organisations should
make their services accessible to all.

- [EU Act](https://digital-strategy.ec.europa.eu/en/policies/web-accessibility)
- [The European Commission's Q&A about the Act](https://ec.europa.eu/social/main.jsp?catId=1202&intPageId=5581&langId=en)
- [Swedish regulations](https://www.digg.se/webbriktlinjer/lagar-och-krav/dos-lagen-och-diggs-foreskrifter)

## Web Content Accessibility Guidelines (WCAG)

https://www.w3.org/WAI/WCAG22/quickref/

WCAG are a set of guidelines for making the web more accessible. The WCAG standards are versioned, with each version
entailing stricter guidelines. The EAA requires compliance with WCAG 2.1.

> WCAG 2.1 was initiated with the goal to improve accessibility guidance for three major groups: users with cognitive or
> learning disabilities, users with low vision, and users with disabilities on mobile devices. Many ways to meet these
> needs were proposed and evaluated, and a set of these were refined by the Working Group. Structural requirements
> inherited from WCAG 2.0, clarity and impact of proposals, and timeline led to the final set of success criteria
> included in this version. The Working Group considers that WCAG 2.1 incrementally advances web content accessibility
> guidance for all these areas, but underscores that not all user needs are met by these guidelines.

WCAG is meant to be backward compatible within the major version numbers, so a site compliant with 2.2 will
automatically be compliant with 2.0 and 2.1.

> WCAG 2.2 was initiated with the goal to continue the work of WCAG 2.1: Improving accessibility guidance for three major
> groups: users with cognitive or learning disabilities, users with low vision, and users with disabilities on
> mobile devices.

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
- https://developer.mozilla.org/en-US/docs/Learn/Accessibility/What_is_accessibility
