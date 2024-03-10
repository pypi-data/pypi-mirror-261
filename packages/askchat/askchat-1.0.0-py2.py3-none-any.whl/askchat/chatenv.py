import click
from pathlib import Path
from askchat import write_config
from dotenv import set_key

# Main environment file
MAIN_ENV_PATH = Path.home() / '.askchat' / '.env'
# Env directory
ENV_PATH = Path.home() / '.askchat' / 'envs'

@click.group()
def cli():
    """chatenv CLI for managing askchat environments."""
    if not ENV_PATH.exists():
        ENV_PATH.mkdir(parents=True)

@cli.command()
def list():
    """List all environment configurations."""
    configs = [env for env in ENV_PATH.glob('*.env')]
    if configs:
        click.echo("Available environments:")
        for config in configs:
            click.echo(f"- {config.stem}")
    else:
        click.echo("No environments found in ~/.askchat/envs.")

@cli.command()
@click.argument('name')
@click.option('-a', '--api-key', default=None, help='API key')
@click.option('-b', '--base-url', default=None, help='Base URL of the API (without suffix `/v1`)')
@click.option('--api-base', default=None, help='Base URL of the API (with suffix `/v1`)')
@click.option('-m', '--model', default=None, help='Model name')
def new(name, api_key, base_url, api_base, model):
    """Create a new environment configuration."""
    config_path = ENV_PATH / f'{name}.env'
    if config_path.exists():
        click.echo(f"Warning: Overwriting existing environment '{name}'.")
        # use click.confirm to ask for user confirmation
        click.confirm("Do you want to continue?", abort=True)
    else:
        click.echo(f"Environment '{name}' created.")
    write_config(config_path, api_key, model, base_url, api_base)

@cli.command()
@click.argument('name', required=False)  # Make 'name' argument optional
@click.option('--default', is_flag=True, help='Delete the default environment configuration')
def delete(name, default):
    """Delete an environment configuration."""
    if default:
        default_config_path = MAIN_ENV_PATH
        if default_config_path.exists():
            default_config_path.unlink()
            click.echo("Default environment configuration deleted.")
        else:
            click.echo("No default environment configuration found.")
    else:
        if not name:
            click.echo("Please specify an environment name or use --default to delete the default configuration.")
            return
        config_path = ENV_PATH / f'{name}.env'
        if config_path.exists():
            config_path.unlink()
            click.echo(f"Environment '{name}' deleted.")
        else:
            click.echo(f"Environment '{name}' not found.")

@cli.command()
@click.argument('name', required=False)
def show(name):
    """Print environment variables. Show default if no name is provided."""
    config_path = ENV_PATH / f'{name}.env' if name else MAIN_ENV_PATH
    if config_path.exists():
        with config_path.open() as f:
            click.echo(f.read())
    else:
        if name:
            click.echo(f"Environment '{name}' not found.")
        else:
            click.echo("No active environment. You can use `chatenv new` to new one.")

@cli.command()
@click.argument('name')
def save(name):
    """Save the current environment variables to a file."""
    if MAIN_ENV_PATH.exists():
        content = MAIN_ENV_PATH.read_text()
        config_path = ENV_PATH / f'{name}.env'
        config_path.write_text(content)
        click.echo(f"Environment '{name}' saved.")
    else:
        click.echo("No active environment to save.")

@cli.command()
@click.argument('name')
def use(name):
    """Activate an environment by replacing the .env file."""
    config_path = ENV_PATH / f'{name}.env'
    if config_path.exists():
        content = config_path.read_text()
        MAIN_ENV_PATH.write_text(content)
        click.echo(f"Environment '{name}' activated.")
    else:
        click.echo(f"Environment '{name}' not found.")

@cli.command()
@click.option('-a', '--api-key', help='API key')
@click.option('-b', '--base-url', help='Base URL of the API (without suffix `/v1`)')
@click.option('--api-base', help='Base URL of the API (with suffix `/v1`)')
@click.option('-m', '--model', help='Model name')
@click.argument('name', required=False)
def config(name, api_key, base_url, api_base, model):
    """Update default .env values."""
    if not any([api_key, base_url, api_base, model]):
        click.echo("No updates made. Provide at least one option to update.")
        return
    config_path = ENV_PATH / f'{name}.env' if name else MAIN_ENV_PATH
    if not config_path.exists():
        click.echo(f"Environment '{config_path}' not found.")
        return
    if api_key:
        set_key(config_path, "OPENAI_API_KEY", api_key)
    if base_url:
        set_key(config_path, "OPENAI_API_BASE_URL", base_url)
    if api_base:
        set_key(config_path, "OPENAI_API_BASE", api_base)
    if model:
        set_key(config_path, "OPENAI_API_MODEL", model)
    click.echo(f"Environment {config_path} updated.")

if __name__ == '__main__':
    cli()
