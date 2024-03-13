def gitinfo(fn, d_repo):
    fmt = '%h»¦«%s»¦«%aN»¦«%aE»¦«%aD'
    breakpoint()  # FIXME BREAKPOINT
    cmd = f'cd "{FLG.axpresent_dir}"; '
    cmd += f"git log --pretty='{fmt}' -n 1 -- 'sets/{fn}'"
