from computer import Computer
from agent import ComputerAgent, LLM


async def main():
    # Start a local macOS VM
    computer = Computer(os_type="macos")
    await computer.run()

    # Or with Cua Cloud Container
    computer = Computer(
        os_type="linux", api_key="your_cua_api_key_here", name="your_container_name_here"
    )

    # Example: Direct control of a macOS VM with Computer
    computer.interface.delay = 0.1  # Wait 0.1 seconds between kb/m actions
    await computer.interface.left_click(100, 200)
    await computer.interface.type_text("Hello, world!")
    screenshot_bytes = await computer.interface.screenshot()

    # Example: Create and run an agent locally using mlx-community/UI-TARS-1.5-7B-6bit
    agent = ComputerAgent(
        model="mlx/mlx-community/UI-TARS-1.5-7B-6bit",
        tools=[computer],
    )
    async for result in agent.run(
        "Find the trycua/cua repository on GitHub and follow the quick start guide"
    ):
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
