from .presidio_helpers import analyzer_engine, get_supported_entities, create_ad_hoc_deny_list_recognizer,create_ad_hoc_regex_recognizer
import logging

logger = logging.getLogger("presidio-init").setLevel(logging.ERROR)

def annotate(text, analysis_results):
    tokens = []
    # sort by start index
    results = sorted(analysis_results, key=lambda x: x.start)
    for i, res in enumerate(results):
        if i == 0:
            tokens.append(text[: res.start])

        # append entity text and entity type
        tokens.append((text[res.start : res.end], res.entity_type))

        # if another entity coming i.e. we're not at the last results element, add text up to next entity
        if i != len(results) - 1:
            tokens.append(text[res.end : results[i + 1].start])
        # if no more entities coming, add all remaining text
        else:
            tokens.append(text[res.end :])
    return tokens


def scan(text, **kwargs):
    # init analyzer instance
    analyzer = analyzer_engine()
    # Set default values for any parameters not provided
    kwargs.setdefault("language", "en")
    kwargs.setdefault("score_threshold", 0.35)
    kwargs.setdefault("nlp_artifacts", None)
    kwargs.setdefault("entities", list(get_supported_entities(analyzer)))
    """Analyze input using Analyzer engine and input arguments (kwargs)."""
    if "entities" not in kwargs or "All" in kwargs["entities"]:
        kwargs["entities"] = None

    if "deny_list" in kwargs and kwargs["deny_list"] is not None:
        ad_hoc_recognizer = create_ad_hoc_deny_list_recognizer(kwargs["deny_list"])
        kwargs["ad_hoc_recognizers"] = [ad_hoc_recognizer] if ad_hoc_recognizer else []
        del kwargs["deny_list"]

    if "regex_params" in kwargs and len(kwargs["regex_params"]) > 0:
        ad_hoc_recognizer = create_ad_hoc_regex_recognizer(*kwargs["regex_params"])
        kwargs["ad_hoc_recognizers"] = [ad_hoc_recognizer] if ad_hoc_recognizer else []
        del kwargs["regex_params"]



    # Call the analyze method with the supported parameters
    return analyzer.analyze(text, **kwargs)


