import re

import data_models.documents as docs
import data_models.api_dtos as api_dtos


def build_guideline_doc(guideline: api_dtos.Guideline) -> docs.GuidelineDocument:
    return docs.GuidelineDocument(
        guideline_id=guideline.guideline_id,
        name=f"{guideline.name}",
        description=_format(guideline.description),
    )


def build_section_doc(
    section: api_dtos.Section,
    guideline_doc: docs.GuidelineDocument,
) -> docs.SectionDocument:
    return docs.SectionDocument(
        section_id=section.section_id,
        guideline_doc=guideline_doc,
        heading=_format(section.heading),
        text=_format(section.text),
        order=section.order,
    )


def build_info_box_doc(
    rec: api_dtos.Recommendation,
    section_doc: docs.SectionDocument,
) -> docs.InfoBoxDocument:
    info_box_doc = docs.InfoBoxDocument(
        rec_id=rec.recommendation_id,
        text=_format(rec.text),
    )
    section_doc.info_box_doc = info_box_doc
    return info_box_doc


def build_rec_doc(
    rec: api_dtos.Recommendation,
    section_doc: docs.SectionDocument,
) -> docs.RecommendationDocument:
    ki = rec.key_info
    return docs.RecommendationDocument(
        rec_id=rec.recommendation_id,
        section_doc=section_doc,
        heading=_format(rec.heading),
        text=_format(rec.text),
        remarks=_format(rec.remarks),
        benefits=_format(ki.benefits, before="Benefits and harms\n"),
        evidence=_format(ki.evidence, before="Certainty of evidence\n"),
        preferences=_format(ki.preferences, before="Values and preferences\n"),
        resources=_format(ki.resources, before="Resources\n"),
        rational=_format(rec.rational, before="Justification\n"),
        advice=_format(rec.advice, before="Practical info\n"),
        order=rec.order,
    )


def build_pico_doc(
    pico: api_dtos.Pico,
    rec_doc: docs.RecommendationDocument,
) -> docs.PicoDocument:
    return docs.PicoDocument(
        pico_id=pico.pico_id,
        rec_doc=rec_doc,
        population=_format(pico.population),
        intervention=_format(pico.intervention),
        comparator=_format(pico.comparator),
        summary=_format(pico.summary),
        order=pico.order,
    )


def build_di_outcome_doc(
    di_outcome: api_dtos.DichotomousOutcome,
    pico_doc: docs.PicoDocument,
) -> docs.DichotomousOutcomeDocument:
    return docs.DichotomousOutcomeDocument(
        di_outcome_id=di_outcome.outcome_id,
        pico_doc=pico_doc,
        outcome=_format(di_outcome.short_name, before="Outcome: "),
        summary=_format(di_outcome.plain_summary_comment, before="Summary:\n"),
        quality_indirectness_comment=_format(
            di_outcome.quality_indirectness_comment, before="Quality indirectness: "
        ),
        quality_of_evidence_comment=_format(
            di_outcome.quality_of_evidence_comment, before="Quality of evidence: "
        ),
        quality_imprecision_comment=_format(
            di_outcome.quality_imprecision_comment, before="Quality imprecision: "
        ),
        sort_order=di_outcome.sort_order,
    )


def build_co_outcome_doc(
    co_outcome: api_dtos.ContinuousOutcome,
    pico_doc: docs.PicoDocument,
) -> docs.ContinuousOutcomeDocument:
    return docs.ContinuousOutcomeDocument(
        co_outcome_id=co_outcome.outcome_id,
        pico_doc=pico_doc,
        outcome=_format(co_outcome.short_name, before="Outcome: "),
        summary=_format(co_outcome.plain_summary_comment, before="Summary:\n"),
        quality_of_evidence_comment=_format(
            co_outcome.quality_of_evidence_comment, before="Quality of evidence: "
        ),
        sort_order=co_outcome.sort_order,
    )


def build_np_outcome_doc(
    np_outcome: api_dtos.NonPoolableOutcome,
    pico_doc: docs.PicoDocument,
) -> docs.NonPoolableOutcomeDocument:
    return docs.NonPoolableOutcomeDocument(
        np_outcome_id=np_outcome.outcome_id,
        pico_doc=pico_doc,
        outcome=_format(np_outcome.short_name, before="Outcome: "),
        summary=_format(np_outcome.plain_summary_comment, before="Summary:\n"),
        quality_of_evidence_comment=_format(
            np_outcome.quality_of_evidence_comment, before="Quality of evidence: "
        ),
        sort_order=np_outcome.sort_order,
    )


def _format(field: str, before: str = "", after: str = "") -> str:
    return f"{before}{_clean_html(field)}{after}" if field else ""


def _clean_html(raw_html: str):
    # Remove HTML tags
    cleanr = re.compile("<.*?>")
    if not raw_html:
        raw_html = ""
    cleantext = re.sub(cleanr, " ", raw_html)

    # Replace newline characters with space
    cleantext = cleantext.replace("\n", "")

    # Replace tab characters with no character
    cleantext = cleantext.replace("\t", "")

    # Replace multiple spaces with single space
    cleantext = re.sub(r"\s+", " ", cleantext)

    # Replace HTML entities
    cleantext = cleantext.replace("&nbsp;", "")

    # Replace <p> tag
    cleantext = cleantext.replace("<p>", "")

    return cleantext
