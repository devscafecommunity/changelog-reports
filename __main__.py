import sys

if "--gui" in sys.argv:
    from gui import launch_gui
    launch_gui()
else:
    from changelog_report import generate_report
    generate_report()