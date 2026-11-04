def summarize_research(topic, articles):

    print("\nCreating research summary...")

    summary = f"\nRESEARCH SUMMARY: {topic}\n"
    summary += "=" * 45 + "\n"

    summary += f"\nThis research focuses on {topic}.\n"

    summary += "\nKEY FINDINGS:\n"

    for number, article in enumerate(articles, start=1):
        summary += f"\n{number}. {article['title']}\n"
        summary += f"{article['snippet']}\n"

    summary += "\nCONCLUSION:\n"
    summary += (
        f"The sources provide an introduction to {topic}. "
        "Further research may be needed to understand the subject "
        "in greater detail.\n"
    )

    return summary