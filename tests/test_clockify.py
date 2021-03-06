import os
import pdb
from .test_gpt_plugin import TestGPTPlugin


class TestClockify(TestGPTPlugin):

    plugin = "clockify"

    def test_load_plugin(self):        
        gpt = self.gpt()
        gpt.gptconfig_settings("plugin", self.plugin)
        token = os.getenv("GP_TRACKING_CLOCKIFY_TOKEN", "")
        gpt.gptconfig_set(self.plugin, "token", token)
        assert gpt.load_plugin() == True, "The plugin do not exists!"

    def test_command_clockify_workspaces(self):
        args = {'clockify_workspaces': True}
        self.cli_params_list( args)

        id, idErr  = self.get_id_stdout()
        args.update({"set": id})
        self.cli_params_set(args)

    def test_command_clockify_projects(self):
        args = {'clockify_projects': True}
        self.cli_params_list( args)

        id, idErr  = self.get_id_stdout()
        args.update({"set": id})
        self.cli_params_set(args)


    def test_time_entry(self): 
        gpt = self.load_plugin()
        parse_defaults =  {"test_time_entry": True}
        gpt.parse.set_defaults(**parse_defaults)
        gpt.cli()