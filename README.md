# BruhBook

`bruhbook` is a Python package designed to interface with OpenAI, allowing users to create captivating short stories complete with custom cover art. This tool is perfect for writers, creators, and anyone interested in generating unique narratives with visually appealing covers.

## Features

- Generate short stories based on specific themes and target audiences.
- Automatically create cover art for the stories.
- Customizable story generation to suit different genres and styles.

## Installation

To install `bruhbook`, simply run:

```bash
pip install bruhbook
```

## Usage

Here is a basic example of how to use `bruhbook` to generate a short story with a cover image:

```py
from bruhbook.bruhbook import BruhBook

# alternativley, you can use a .env file with a `OPENAI_API_KEY` variable set to your key
bb = BruhBook(
    api_key=<openai_api_key>,
    create_cover_image=True,
    wipe_files=False
)

story_type = "A cyberpunk knight fighting his way through a hellish landscape. Flames, lava, dark, alien like plasma monsters"
target_audience = "Highschoolers / Adults"

bb.generate_story(
    story_type=story_type,
    target_audience=target_audience
)
```

## Requirements

- Python 3.11 or later

## Documentation

🚧 Under Construciton 🚧

## Contributing

🚧 Under Construction 🚧

## License

`bruhbook` is licensed under the Apache License. See the [LICENSE](LICENSE) file for more details.
