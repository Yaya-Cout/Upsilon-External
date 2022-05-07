# External applications documentation

## Creating a new project

To create a new project, you just need to:

1. Create a new directory with the name of your project. You can copy the Example project to get started.
2. Add your project to the Makefile. You just need copy the `apps/Example/app.elf` target then rename the `Example` to your project name.
3. Add your project to the `apps/apps.js` file.
4. To flash your project, you just need to run the `make app-name_flash` command.
5. It's done! :tada:

## Editing a project

To edit a project, you just need to open your project directory and edit the files.
To flash your project, you just need to run the `make app-name_flash` command in the root directory (not in your app directory).

If you want to see the external applications documentation, you have the `api/extapi.h` file, which contains is the list of all the external applications commands and their description.

## Publishing your app

To publish your app, please follow the steps below:

1. First, you need to fork the [Github repository](https://github.com/UpsilonNumworks/Upsilon-External).
2. After that, you can create a new branch and push it to your fork.
3. Then, create a pull request.
4. When the pull request is merged, the app will be published.
5. Done :tada:

If you have any questions, please join the [Omega Community Discord server](https://discord.gg/hnEqPzAJzn).
