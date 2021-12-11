import os
from pathlib import Path

# import nbgrader_context as nbcon

#gradebook = os.environ["e213_gradebook"]
gradebook = "birwin_gradebook.db"
gradebook = "clm_gradebook.db"
gradebook = "e211_gradebook.db"

root_dir = Path("/home/jovyan/work")
assign_db = root_dir / gradebook
#exchange_dir = nbcon.root_dir / Path("exchange")
exchange_dir = root_dir / "exchange"
print(f"setting root to {root_dir}")

print(f"assignment db is {assign_db}")

c = get_config()  # noqa

c.CourseDirectory.db_url = f"sqlite:///{assign_db}"
c.CourseDirectory.root = str(root_dir)
c.ExecutePreprocessor.timeout  = 300
c.CourseDirectory.course_id = "e211"
c.Exchange.root = str(exchange_dir)

# Apply this regular expression to the extracted file filename (absolute path)
c.FileNameCollectorPlugin.named_regexp = (
    r".*_(?P<student_id>\w+)_attempt_" "(?P<file_id>.*)"
)
