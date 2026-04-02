import gifos
import os
from datetime import datetime
from zoneinfo import ZoneInfo

# bundled font from the gifos package
FONT_PATH = os.path.join(os.path.dirname(gifos.__file__), "gohufont-uni-14.pil")


def main():
    t = gifos.Terminal(750, 500, 15, 15, FONT_PATH, 15)

    year_now = datetime.now(ZoneInfo("Europe/Moscow")).strftime("%Y")
    time_now = datetime.now(ZoneInfo("Europe/Moscow")).strftime(
        "%a %b %d %I:%M:%S %p MSK %Y"
    )

    # ─── BIOS SCREEN ───────────────────────────────────────────────────────────
    t.toggle_show_cursor(False)
    t.gen_text("", 1, count=20)
    t.gen_text("ALTUFETCH Modular BIOS v666.0", 1)
    t.gen_text(
        f"Copyright (C) {year_now}, \x1b[31maltushki_inc\x1b[0m  All wrongs reserved.", 2
    )
    t.gen_text("\x1b[94mGitHub Profile Terminal  Rev 0x1337\x1b[0m", 4)
    t.gen_text("BasementCPU(tm)  1.5 kek/s  |  RAM: che nashyol, to i vstavil", 6)
    t.gen_text(
        "Press \x1b[94mDEL\x1b[0m to enter SETUP  |  \x1b[94mF1\x1b[0m to touch grass",
        t.num_rows,
    )

    # memory test
    for i in range(0, 65653, 7168):
        t.delete_row(7)
        if i < 30000:
            t.gen_text(f"Memory Test: {i}", 7, count=2, contin=True)
        else:
            t.gen_text(f"Memory Test: {i}", 7, contin=True)
    t.delete_row(7)
    t.gen_text(
        "Memory Test: 64KB OK  (brain: 0KB  barely OK)", 7, count=10, contin=True
    )
    t.gen_text("", 11, count=10, contin=True)

    # ─── BOOT ──────────────────────────────────────────────────────────────────
    t.clear_frame()
    t.gen_text("Initiating Boot Sequence ", 1, contin=True)
    t.gen_typing_text(".....", 1, contin=True)

    # ─── LOGIN SCREEN ──────────────────────────────────────────────────────────
    t.clear_frame()
    t.clone_frame(5)
    t.toggle_show_cursor(False)
    t.gen_text("\x1b[93mALTUFETCH OS v666  (tty1)\x1b[0m", 1, count=5)
    t.gen_text("login: ", 3, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("sykoco", 3, contin=True)
    t.gen_text("", 4, count=5)
    t.toggle_show_cursor(False)
    t.gen_text("password: ", 4, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("***altUsha69***", 4, contin=True)
    t.toggle_show_cursor(False)
    t.gen_text(f"Last login: {time_now} on tty1", 6)

    # clear cmd with fake syntax highlighting
    t.gen_prompt(7, count=5)
    prompt_col = t.curr_col
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mclea", 7, contin=True)
    t.delete_row(7, prompt_col)
    t.gen_text("\x1b[92mclear\x1b[0m", 7, count=3, contin=True)

    # ─── FETCH STATS ───────────────────────────────────────────────────────────
    try:
        git_stats = gifos.utils.fetch_github_stats("sykoco")
        top_langs = [lang[0] for lang in git_stats.languages_sorted]
        commits = git_stats.total_commits_last_year
        stars = git_stats.total_stargazers
        contribs = git_stats.total_repo_contributions
        langs_str = ", ".join(top_langs[:4]) if top_langs else "python"
    except Exception as e:
        print(f"WARN: failed to fetch GitHub stats: {e}")
        commits, stars, contribs, langs_str = "??", "??", "??", "python"

    info = f"""\
 \x1b[30;105m sykoco@GitHub \x1b[0m
 \x1b[90m\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\x1b[0m
 \x1b[96mOS         \x1b[93mwindows / basement\x1b[0m
 \x1b[96mType       \x1b[95maltushki s 3 razmerom\x1b[0m
 \x1b[96mStatus     \x1b[91mnot sleeping  (404)\x1b[0m
 \x1b[96mActivity   \x1b[92mpython  /  03:00 AM\x1b[0m
 \x1b[96mGoal       \x1b[93msleep  (perpetually failed)\x1b[0m
 \x1b[90m\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\x1b[0m
 \x1b[96mCommits ({int(year_now) - 1})  \x1b[93m{commits}\x1b[0m
 \x1b[96mStars       \x1b[93m{stars}\x1b[0m
 \x1b[96mContribs    \x1b[93m{contribs}\x1b[0m
 \x1b[96mLanguages   \x1b[93m{langs_str}\x1b[0m
 \x1b[90m\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\x1b[0m
 \x1b[90m$ sudo wake_up   ->  command not found\x1b[0m
 \x1b[90m$ sleep 8h       ->  alarm bot is running\x1b[0m
"""

    t.clear_frame()
    t.gen_prompt(1)
    prompt_col = t.curr_col
    t.clone_frame(10)
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mfetch.s", 1, contin=True)
    t.delete_row(1, prompt_col)
    t.gen_text("\x1b[92mfetch.sh\x1b[0m", 1, contin=True)
    t.gen_typing_text(" -u sykoco", 1, contin=True)

    t.toggle_show_cursor(False)
    t.gen_text(info, 2, count=5, contin=True)
    t.gen_prompt(t.curr_row)
    t.toggle_show_cursor(True)
    t.gen_typing_text(
        "\x1b[92m# go touch grass  (RuntimeError: grass.exe not found)",
        t.curr_row,
        contin=True,
    )
    t.gen_text("", t.curr_row, count=120, contin=True)

    t.gen_gif()
    print("INFO: output.gif generated successfully")


if __name__ == "__main__":
    main()
