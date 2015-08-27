from datetime import datetime
import sys

TEMPLATE = """
{title}
{hashes}

:date: {year}-{month}-{day} {hour}:{minute:02d}
:tags:
:category:
:slug: {slug}
:status: draft



"""

def make_entry(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    f_create = "content/{}_{:0>2}_{:0>2}_{}.rst".format(
        today.year, today.month, today.day, slug
    )
    t = TEMPLATE.strip().format(title=title,
                                hashes='#' * len(title),
                                year=today.year,
                                month=today.month,
                                day=today.hour,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug)

    with open(f_create, 'w') as out_file:
        out_file.write(t)
    print("File created -> " + f_create)

if __name__ == "__main__":

    if len(sys.argv) > 1:
        make_entry(sys.argv[1])
    else:
        print "No title given"
