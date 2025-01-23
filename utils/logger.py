import logging

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("cicd_tool.log"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger("CI/CD Tool")
