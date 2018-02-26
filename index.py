# from flask import Flask, request
import connexion
import subprocess

def run_tooldog(tool_id, format="galaxy", run=None):
    # run tooldog as a child process

    # FIXME: until docker will set up ---------V
    run = "--{}".format(run) if run else "--annotate"

    process = subprocess.Popen(["tooldog",
                                "--{}".format(format),
                                run, tool_id],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

    # get the result
    output = "".join(map(lambda x: x.decode("utf-8"), process.stdout.readlines()))

    # TODO: some check for errors (for example, if stderr is not empty)
    code = 200

    # show the result as a response
    return output, code


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, specification_dir='swagger/')
    app.add_api('my_api.yaml')
    app.run(debug=True)
