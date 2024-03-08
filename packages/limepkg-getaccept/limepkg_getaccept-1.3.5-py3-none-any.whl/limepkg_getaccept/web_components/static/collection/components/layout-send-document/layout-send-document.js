import { Component, h, State, Prop, Event } from '@stencil/core';
import { EnumViews } from '../../models/EnumViews';
import { fetchDealValue } from 'src/services';
export class LayoutSendDocument {
  constructor() {
    this.documentName = '';
    this.value = 0;
    this.smartReminder = false;
    this.sendLinkBySms = false;
    this.documentVideo = false;
    this.handleChangeDocumentName =
      this.handleChangeDocumentName.bind(this);
    this.handleChangeValue = this.handleChangeValue.bind(this);
    this.handleChangeSmartReminder =
      this.handleChangeSmartReminder.bind(this);
    this.handleChangeSendLinkBySms =
      this.handleChangeSendLinkBySms.bind(this);
    this.handleAddVideo = this.handleAddVideo.bind(this);
    this.handleRemoveVideo = this.handleRemoveVideo.bind(this);
  }
  async componentWillLoad() {
    this.documentName = this.fileName();
    this.setNewDocumentName.emit(this.documentName);
    this.value = this.document.value || 0;
    this.smartReminder = this.document.is_reminder_sending;
    this.sendLinkBySms = this.document.is_sms_sending;
    this.documentVideo = this.document.video_id !== '';
    await this.loadObjectValue();
  }
  componentDidUpdate() {
    this.value = this.document.value;
    this.documentName = this.document.name || this.fileName();
  }
  render() {
    return [
      h("div", { class: "send-document-container" },
        h("div", { class: "send-document-prepare-container" },
          h("h3", null, "Prepare sending"),
          h("limel-flex-container", { align: "stretch" },
            h("limel-input-field", { label: "Document Name", value: this.documentName, onChange: this.handleChangeDocumentName }),
            h("limel-input-field", { label: "Value", value: this.value.toString(), onChange: this.handleChangeValue })),
          h("div", null,
            h("h4", null, "Document engagement"),
            this.documentVideo ? (h("div", null,
              h("div", { class: "video-is-added" },
                h("limel-icon", { name: "tv_show", size: "large", class: "video-is-added-icon" }),
                h("span", null, "Video is added"),
                h("limel-icon", { class: "video-remove-icon", name: "multiply", size: "small", onClick: this.handleRemoveVideo })))) : (h("limel-button", { class: "add-video-button", primary: true, label: "Add Video introduction", onClick: this.handleAddVideo })),
            h("limel-checkbox", { label: "Send smart reminders", id: "SmartReminder", checked: this.smartReminder, onChange: this.handleChangeSmartReminder }),
            h("limel-checkbox", { label: "Send link by SMS", id: "SendLinkBySMS", checked: this.sendLinkBySms, onChange: this.handleChangeSendLinkBySms }))),
        h("div", { class: "send-document-email-container" },
          h("create-email", { document: this.document }))),
    ];
  }
  async loadObjectValue() {
    // eslint-disable-next-line camelcase
    const { id: record_id, limetype } = this.context;
    try {
      const value = await fetchDealValue(this.platform, this.session, limetype, record_id);
      this.setDocumentValue.emit(value);
    }
    catch (e) {
      this.errorHandler.emit('Could not fetch lime object...');
    }
  }
  fileName() {
    if (this.limeDocument) {
      return this.limeDocument.text;
    }
    else if (this.template) {
      return this.template.text;
    }
    else {
      return '';
    }
  }
  handleChangeDocumentName(event) {
    this.setNewDocumentName.emit(event.detail);
  }
  handleChangeValue(event) {
    this.setDocumentValue.emit(event.detail);
  }
  handleChangeSmartReminder(event) {
    this.setSmartReminder.emit(event.detail);
  }
  handleChangeSendLinkBySms(event) {
    this.setIsSmsSending.emit(event.detail);
  }
  handleAddVideo() {
    // should open select video view
    this.changeView.emit(EnumViews.videoLibrary);
  }
  // TODO: function for uploading file, in advance
  // private async handleChange(event: CustomEvent<FileInfo>) {
  //     this.fileValue = event.detail;
  //     const { data, success } = await uploadFile(
  //         this.platform,
  //         this.session,
  //         this.fileValue
  //     );
  //     console.log(data, success);
  // }
  handleRemoveVideo() {
    this.removeVideo.emit();
    this.documentVideo = false;
  }
  static get is() { return "layout-send-document"; }
  static get encapsulation() { return "shadow"; }
  static get originalStyleUrls() { return {
    "$": ["layout-send-document.scss"]
  }; }
  static get styleUrls() { return {
    "$": ["layout-send-document.css"]
  }; }
  static get properties() { return {
    "document": {
      "type": "unknown",
      "mutable": false,
      "complexType": {
        "original": "IDocument",
        "resolved": "IDocument",
        "references": {
          "IDocument": {
            "location": "import",
            "path": "../../types/Document"
          }
        }
      },
      "required": false,
      "optional": false,
      "docs": {
        "tags": [],
        "text": ""
      }
    },
    "template": {
      "type": "unknown",
      "mutable": false,
      "complexType": {
        "original": "IListItem",
        "resolved": "IListItem",
        "references": {
          "IListItem": {
            "location": "import",
            "path": "../../types/ListItem"
          }
        }
      },
      "required": false,
      "optional": false,
      "docs": {
        "tags": [],
        "text": ""
      }
    },
    "limeDocument": {
      "type": "unknown",
      "mutable": false,
      "complexType": {
        "original": "IListItem",
        "resolved": "IListItem",
        "references": {
          "IListItem": {
            "location": "import",
            "path": "../../types/ListItem"
          }
        }
      },
      "required": false,
      "optional": false,
      "docs": {
        "tags": [],
        "text": ""
      }
    },
    "platform": {
      "type": "unknown",
      "mutable": false,
      "complexType": {
        "original": "LimeWebComponentPlatform",
        "resolved": "LimeWebComponentPlatform",
        "references": {
          "LimeWebComponentPlatform": {
            "location": "import",
            "path": "@limetech/lime-web-components"
          }
        }
      },
      "required": false,
      "optional": false,
      "docs": {
        "tags": [],
        "text": ""
      }
    },
    "session": {
      "type": "unknown",
      "mutable": false,
      "complexType": {
        "original": "ISession",
        "resolved": "ISession",
        "references": {
          "ISession": {
            "location": "import",
            "path": "../../types/Session"
          }
        }
      },
      "required": false,
      "optional": false,
      "docs": {
        "tags": [],
        "text": ""
      }
    },
    "context": {
      "type": "unknown",
      "mutable": false,
      "complexType": {
        "original": "LimeWebComponentContext",
        "resolved": "LimeWebComponentContext",
        "references": {
          "LimeWebComponentContext": {
            "location": "import",
            "path": "@limetech/lime-web-components"
          }
        }
      },
      "required": false,
      "optional": false,
      "docs": {
        "tags": [],
        "text": ""
      }
    }
  }; }
  static get states() { return {
    "documentName": {},
    "value": {},
    "smartReminder": {},
    "sendLinkBySms": {},
    "documentVideo": {}
  }; }
  static get events() { return [{
      "method": "setNewDocumentName",
      "name": "setNewDocumentName",
      "bubbles": true,
      "cancelable": true,
      "composed": true,
      "docs": {
        "tags": [],
        "text": ""
      },
      "complexType": {
        "original": "string",
        "resolved": "string",
        "references": {}
      }
    }, {
      "method": "setDocumentValue",
      "name": "setDocumentValue",
      "bubbles": true,
      "cancelable": true,
      "composed": true,
      "docs": {
        "tags": [],
        "text": ""
      },
      "complexType": {
        "original": "number",
        "resolved": "number",
        "references": {}
      }
    }, {
      "method": "setIsSmsSending",
      "name": "setIsSmsSending",
      "bubbles": true,
      "cancelable": true,
      "composed": true,
      "docs": {
        "tags": [],
        "text": ""
      },
      "complexType": {
        "original": "boolean",
        "resolved": "boolean",
        "references": {}
      }
    }, {
      "method": "setSmartReminder",
      "name": "setSmartReminder",
      "bubbles": true,
      "cancelable": true,
      "composed": true,
      "docs": {
        "tags": [],
        "text": ""
      },
      "complexType": {
        "original": "boolean",
        "resolved": "boolean",
        "references": {}
      }
    }, {
      "method": "errorHandler",
      "name": "errorHandler",
      "bubbles": true,
      "cancelable": true,
      "composed": true,
      "docs": {
        "tags": [],
        "text": ""
      },
      "complexType": {
        "original": "string",
        "resolved": "string",
        "references": {}
      }
    }, {
      "method": "changeView",
      "name": "changeView",
      "bubbles": true,
      "cancelable": true,
      "composed": true,
      "docs": {
        "tags": [],
        "text": ""
      },
      "complexType": {
        "original": "any",
        "resolved": "any",
        "references": {}
      }
    }, {
      "method": "removeVideo",
      "name": "removeVideo",
      "bubbles": true,
      "cancelable": true,
      "composed": true,
      "docs": {
        "tags": [],
        "text": ""
      },
      "complexType": {
        "original": "any",
        "resolved": "any",
        "references": {}
      }
    }]; }
}
