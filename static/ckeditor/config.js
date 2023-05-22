/**
 * @license Copyright (c) 2003-2023, CKSource Holding sp. z o.o. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function (config) {
  // Define changes to default configuration here.
  // For complete reference see:
  // https://ckeditor.com/docs/ckeditor4/latest/api/CKEDITOR_config.html

  // The toolbar groups arrangement, optimized for two toolbar rows.
  config.toolbarGroups = [
    { name: "clipboard", groups: ["clipboard", "undo"] },
    { name: "editing", groups: ["find", "selection", "spellchecker"] },
    { name: "links" },
    { name: "insert" },
    { name: "forms" },
    { name: "tools" },
    { name: "document", groups: ["mode", "document", "doctools"] },
    { name: "others" },
    "/",
    { name: "basicstyles", groups: ["basicstyles", "cleanup"] },
    {
      name: "paragraph",
      groups: ["list", "indent", "blocks", "align", "bidi"],
    },
    { name: "styles" },
    { name: "colors" },
    { name: "about" },
  ];

  // Remove some buttons provided by the standard plugins, which are
  // not needed in the Standard(s) toolbar.
  config.removeButtons = "Underline,Subscript,Superscript";

  // Set the most common block elements.
  config.format_tags = "p;h1;h2;h3;pre";

  // Simplify the dialog windows.
  config.removeDialogTabs = "image:advanced;link:advanced";
};

CKEDITOR.on("instanceReady", function (ev) {
  with (ev.editor.dataProcessor.writer) {
    setRules("p", {
      indent: false,
      breakBeforeOpen: false,
      breakAfterOpen: false,
      breakBeforeClose: false,
      breakAfterClose: false,
    });
    setRules("h1", {
      indent: false,
      breakBeforeOpen: false,
      breakAfterOpen: false,
      breakBeforeClose: false,
      breakAfterClose: false,
    });
    setRules("h2", {
      indent: false,
      breakBeforeOpen: false,
      breakAfterOpen: false,
      breakBeforeClose: false,
      breakAfterClose: false,
    });
    setRules("h3", {
      indent: false,
      breakBeforeOpen: false,
      breakAfterOpen: false,
      breakBeforeClose: false,
      breakAfterClose: false,
    });
    setRules("h4", {
      indent: false,
      breakBeforeOpen: false,
      breakAfterOpen: false,
      breakBeforeClose: false,
      breakAfterClose: false,
    });
    setRules("h5", {
      indent: false,
      breakBeforeOpen: false,
      breakAfterOpen: false,
      breakBeforeClose: false,
      breakAfterClose: false,
    });
    setRules("div", {
      indent: false,
      breakBeforeOpen: false,
      breakAfterOpen: false,
      breakBeforeClose: false,
      breakAfterClose: false,
    });
    setRules("table", {
      indent: false,
      breakBeforeOpen: false,
      breakAfterOpen: false,
      breakBeforeClose: false,
      breakAfterClose: false,
    });
    setRules("tr", {
      indent: false,
      breakBeforeOpen: false,
      breakAfterOpen: false,
      breakBeforeClose: false,
      breakAfterClose: false,
    });
    setRules("td", {
      indent: false,
      breakBeforeOpen: false,
      breakAfterOpen: false,
      breakBeforeClose: false,
      breakAfterClose: false,
    });
    setRules("iframe", {
      indent: false,
      breakBeforeOpen: false,
      breakAfterOpen: false,
      breakBeforeClose: false,
      breakAfterClose: false,
    });
    setRules("li", {
      indent: false,
      breakBeforeOpen: false,
      breakAfterOpen: false,
      breakBeforeClose: false,
      breakAfterClose: false,
    });
    setRules("ul", {
      indent: false,
      breakBeforeOpen: false,
      breakAfterOpen: false,
      breakBeforeClose: false,
      breakAfterClose: false,
    });
    setRules("ol", {
      indent: false,
      breakBeforeOpen: false,
      breakAfterOpen: false,
      breakBeforeClose: false,
      breakAfterClose: false,
    });
  }
});
