071-simplify_path
#################

:date: 2015-11-2 22:35
:tags:
:category: LeetCode
:slug: 071-simplify_path

`LeetCode Problem Link <https://leetcode.com/problems/simplify-path/>`_

The thing to note that if you are currently at the root directory already, then trying go to the parent directory
does not move where you are. You will still be in the root directory.

.. code-block:: java

    public String simplifyPath(String path) {
        String[] tokens = path.split("/");
        StringBuffer sb = new StringBuffer();
        List<String> dirs = new ArrayList<String>();

        if (tokens.length == 0)
            return "/";

        for (int i=1; i<tokens.length; i++) {
            String token = tokens[i];

            if (token.equals(".") || token.length()==0) {
                // ignore
            }
            else if (token.equals("..")) {
                //
                if (!dirs.isEmpty()) {
                    dirs.remove(dirs.size() - 1);
                }
            }
            else {
                dirs.add(token);
            }
        }

        if (dirs.isEmpty()) {
            return "/";
        }

        System.out.println(dirs.size());

        for (String dir: dirs) {
            sb.append("/");
            sb.append(dir);
        }

        return sb.toString();
    }