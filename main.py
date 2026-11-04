from research import search_research
from summarize import summarize_research
from pdf_report import create_pdf


def main():

    while True:

        print("\n" + "=" * 45)
        print("          AI RESEARCH AGENT")
        print("=" * 45)

        print("\n1. Research a new topic")
        print("2. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":

            topic = input("\nWhat would you like to research? ").strip()

            if not topic:
                print("Please enter a research topic.")
                continue

            print(f"\nSearching for: {topic}")
            print("Please wait...\n")

            articles = search_research(topic)

            if not articles:
                print("No research results found.")
                continue

            print("\nRESEARCH RESULTS")
            print("=" * 45)

            for number, article in enumerate(articles, start=1):

                print(f"\n{number}. {article['title']}")
                print(article['snippet'])
                print(f"Source: {article['url']}")

            summary = summarize_research(topic, articles)

            print("\nAI RESEARCH SUMMARY")
            print("=" * 45)
            print(summary)

            create_pdf(topic, articles, summary)

            print("\nYour research report has been saved!")

        elif choice == "2":

            print("\nThank you for using AI Research Agent!")
            break

        else:
            print("\nInvalid option. Please choose 1 or 2.")



if __name__ == "__main__":
    main()