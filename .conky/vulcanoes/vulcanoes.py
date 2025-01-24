import os
import feedparser
# Lock file to tell conky that the script is running
lock_file = "/tmp/script_eq.lock"
try:
    # Create lock file
    open(lock_file, 'w').close()
    qta = 15
    ################################ get your HOME name automatically
    homepath = os.environ['HOME']
    homename = homepath
    homename = homename[6:]
    ################################ set the paths for the file
    conkypath = '/.conky/'
    vulcanoesF = "/home/" + homename + conkypath + 'vulcanoes/vulcanoesRSS.txt'
    # Parse Upwork URL
    feedV = feedparser.parse('https://www.volcanodiscovery.com/volcanonews.rss')
    fo = open(vulcanoesF, 'w')
    for i in range(0,qta):
        temp = feedV.entries[i].title
        fo.write('- {}\n'.format(temp))
    fo.close()
except Exception as e:
    # Manage exceptions (optional)
    filelockerror = (f"Error during script execution: {e}")
finally:
    # remove lock file
    try:
        os.remove(lock_file)
    except FileNotFoundError:
        pass  # file already removed
