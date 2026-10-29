# Autonomous ML Lab

Daily AI agent that proposes small improvements to ML projects using GitHub Actions and OpenAI. Changes appear as pull requests for human review.

## Setup

1. Add your OpenAI API key as repository Actions secret `OPENAI_API_KEY`.
2. Under Settings > Actions > General, allow GitHub Actions to create pull requests and enable read/write workflow permissions.
3. Run Actions > Daily ML Agent > Run workflow to test.
4. Review generated PRs before merging.

The scheduled run is 16:17 UTC daily, which corresponds to 09:17 Pacific in daylight saving time and 08:17 in standard time. GitHub schedules may be delayed. API usage is billed separately.
