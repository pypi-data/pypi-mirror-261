import download from "downloadjs"

import {shortFileTitle} from "../../common"
import {createSlug} from "../tools/file"
import {XmlZip} from "../tools/xml_zip"
import {removeHidden, fixTables} from "../tools/doc_content"
import {moveFootnoteComments} from "./tools"
import {DocxExporterCitations} from "./citations"
import {DocxExporterComments} from "./comments"
import {DocxExporterImages} from "./images"
import {DocxExporterRender} from "./render"
import {DocxExporterRichtext} from "./richtext"
import {DocxExporterRels} from "./rels"
import {DocxExporterFootnotes} from "./footnotes"
import {DocxExporterMetadata} from "./metadata"
import {DocxExporterMath} from "./math"
import {DocxExporterTables} from "./tables"
import {DocxExporterLists} from "./lists"

/*
Exporter to Office Open XML docx (Microsoft Word)
*/

/*
TODO:
* - Export tracked changes
* - Export document language
* - Templating of tag/contributor output
*/

export class DocxExporter {
    constructor(doc, templateUrl, bibDB, imageDB, csl) {
        this.doc = doc
        this.templateUrl = templateUrl
        this.bibDB = bibDB
        this.imageDB = imageDB
        this.csl = csl

        this.pmBib = false
        this.docContent = false
        this.docTitle = false
        this.mimeType = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    }


    init() {
        this.docContent = moveFootnoteComments(fixTables(removeHidden(this.doc.content)))
        this.docTitle = shortFileTitle(this.doc.title, this.doc.path)
        this.tables = new DocxExporterTables(this)
        this.math = new DocxExporterMath(this)
        this.metadata = new DocxExporterMetadata(this, this.docContent)
        this.footnotes = new DocxExporterFootnotes(this, this.docContent)
        this.render = new DocxExporterRender(this, this.docContent)
        this.rels = new DocxExporterRels(this, "document")
        this.images = new DocxExporterImages(this, this.imageDB, this.rels, this.docContent)
        this.lists = new DocxExporterLists(this, this.rels, this.docContent)
        this.citations = new DocxExporterCitations(this, this.bibDB, this.csl, this.docContent)
        this.comments = new DocxExporterComments(this, this.doc.comments, this.docContent)
        this.richtext = new DocxExporterRichtext(
            this,
            this.rels,
            this.citations,
            this.images,
            this.comments,
        )

        this.xml = new XmlZip(
            this.templateUrl,
            this.mimeType
        )

        return this.xml.init().then(
            () => this.citations.init()
        ).then(
            () => {
                this.pmBib = this.citations.pmBib
                return this.metadata.init()
            }
        ).then(
            () => this.tables.init()
        ).then(
            () => this.math.init()
        ).then(
            () => this.render.init()
        ).then(
            () => this.rels.init()
        ).then(
            () => this.images.init()
        ).then(
            () => this.comments.init()
        ).then(
            () => this.lists.init()
        ).then(
            () => this.footnotes.init()
        ).then(
            () => {
                this.render.getTagData(this.pmBib)
                this.render.render()
                return this.xml.prepareBlob()
            }
        ).then(
            blob => this.download(blob)
        )
    }
    download(blob) {
        return download(blob, createSlug(this.docTitle) + ".docx", this.mimeType)
    }

}
