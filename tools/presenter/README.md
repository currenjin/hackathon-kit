# Presenter

Two-window slide presenter. One window shows only the slide (send it to the projector). The other shows the current slide, the next slide, what to say on this slide, and a timer. No server and no install: open the HTML file in Chrome.

## Use

1. Render slides to images (one PNG per slide, 16:9).
2. Write a deck data file that sets `window.DECK` (see below). Keep it in the event workspace, not here.
3. Open `tools/presenter/presenter.html`. Pick a registered deck (listed in `decks.js`) or upload a folder that holds the deck data file and its slide images. You can also open `presenter.html?deck=<path>` directly.
4. Click **Open audience window**, drag that window to the projector, then click anywhere in it (or press **F**). This uses page full screen, which hides the address bar; the macOS green button does not.
5. Drive from the presenter window: → / Space next, ← previous, T timer.

## Deck data

```js
window.DECK = {
  title: 'My talk',
  base: '../deck/',            // optional; images resolve against this, relative to the data file
  slides: [
    { img: 'slide-1.png', title: 'Cover', screen: 'What the audience sees', say: ['Line one.', 'Line two.'], must: ['113 checks'], seconds: 15 },
  ],
  questions: ['Why X? → short answer'],  // shown on the last slide
};
```

`must` lists facts or numbers that have to be said exactly. `seconds` is the target time; the slide timer turns amber at 80% and red when over.

## Make an event deck

Run `/present` in the kit. It reads the `/deck` slide images and the `/pitch` script, writes `workspace/<event>/output/presenter/<lang>/` (`deck.js` + images, image names without paths so the folder uploads as is), and adds one line to `decks.js`.

## Notes

- The audience window is opened by the presenter page, so both stay in sync without a server.
- If the browser blocks pop-ups, allow them for the file once.
- Chrome blocks `fetch` on `file://`, which is why the deck data is a `.js` file loaded with a script tag.
