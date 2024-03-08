from HA_cfg_cleaner_DiosWolf.data_classes_json.file_config import ConfigurationFile
from HA_cfg_cleaner_DiosWolf.data_classes_json.instructions import Instructions, ChangeCfgAddons
from HA_cfg_cleaner_DiosWolf.files_editors.addons_editor import AddonsEditor
from HA_cfg_cleaner_DiosWolf.files_editors.automations_editor import AutomationsEditor
from HA_cfg_cleaner_DiosWolf.files_editors.editor_restore_state import EditorRestoreFile
from HA_cfg_cleaner_DiosWolf.files_editors.fileIO_cls import FileIO
from HA_cfg_cleaner_DiosWolf.files_editors.file_folder_editor_cls import (
    FileFoldersEditor,
)
from HA_cfg_cleaner_DiosWolf.files_editors.find_in_files_cls import FindInAllFiles
from HA_cfg_cleaner_DiosWolf.files_editors.integrations_cls import IntegrationsEditor
from HA_cfg_cleaner_DiosWolf.files_editors.script_editor_cls import ScriptsEditor


class InstructionsExecute:
    def __init__(
        self,
        all_instructions: Instructions,
        file_io: FileIO,
        all_configs: ConfigurationFile,
    ):
        self.all_instructions = all_instructions
        self.all_configs = all_configs
        self.file_io = file_io

    def del_integrations(self):
        ids_list: list[str] = self.all_instructions.delete_integrations.ids_list
        for configuration in self.all_configs.configurations:
            full_cfg = self.file_io.read_with_type(
                configuration.path + configuration.filename, configuration.type_cfg
            )
            integration_editor = IntegrationsEditor(configuration, full_cfg)

            try:
                new_cgf = integration_editor.delete_integration(ids_list)
                self.file_io.write_with_type(
                    configuration.path + configuration.filename,
                    new_cgf,
                    configuration.type_cfg,
                )
            except Exception as exp:
                print(exp)

    def enable_integrations(self):
        ids_list: list[str] = self.all_instructions.enable_integration.ids_list

        for configuration in self.all_configs.configurations:
            full_cfg = self.file_io.read_with_type(
                configuration.path + configuration.filename, configuration.type_cfg
            )
            integration_editor = IntegrationsEditor(configuration, full_cfg)
            new_cgf = integration_editor.disable_enable_integration(
                ids_list, configuration.on_integration
            )
            self.file_io.write_with_type(
                configuration.path + configuration.filename,
                new_cgf,
                configuration.type_cfg,
            )

    def disable_integrations(self):
        ids_list: list[str] = self.all_instructions.disable_integration.ids_list

        for configuration in self.all_configs.configurations:
            full_cfg = self.file_io.read_with_type(
                configuration.path + configuration.filename, configuration.type_cfg
            )
            integration_editor = IntegrationsEditor(configuration, full_cfg)

            new_cgf = integration_editor.disable_enable_integration(
                ids_list, configuration.off_integration
            )
            self.file_io.write_with_type(
                configuration.path + configuration.filename,
                new_cgf,
                configuration.type_cfg,
            )

    def del_automations(self):
        ids_list: list[str] = self.all_instructions.delete_automations.ids_list

        for configuration in self.all_configs.automations_cfg:

            full_cfg = self.file_io.read_with_type(
                configuration.path + configuration.filename, configuration.type_cfg
            )

            try:
                automation_editor = AutomationsEditor(configuration, full_cfg)
                new_cgf = automation_editor.delete_automation(ids_list)

                self.file_io.write_with_type(
                    configuration.path + configuration.filename,
                    new_cgf,
                    configuration.type_cfg,
                )
            except Exception as exp:
                print(exp)

    def del_automations_restore_state(self):
        ids_list: list[str] = self.all_instructions.delete_automations.ids_list
        full_cfg = self.file_io.read_with_type(
            self.all_configs.config_restore_state.path
            + self.all_configs.config_restore_state.filename,
            self.all_configs.config_restore_state.type_cfg,
        )

        automation_editor = EditorRestoreFile(
            self.all_configs.config_restore_state, full_cfg
        )
        new_cgf = automation_editor.del_automation_restore_state(ids_list)

        self.file_io.write_with_type(
            self.all_configs.config_restore_state.path
            + self.all_configs.config_restore_state.filename,
            new_cgf,
            self.all_configs.config_restore_state.type_cfg,
        )

    def disable_automations(self):
        ids_list: list[str] = self.all_instructions.disable_automations.ids_list
        for configuration in self.all_configs.automations_cfg:

            if configuration.config_id == "entity_registry":
                full_cfg = self.file_io.read_with_type(
                    configuration.path + configuration.filename, configuration.type_cfg
                )

                if self.all_instructions.disable_automations.host_info is not None:
                    host_info = self.all_instructions.disable_automations.host_info

                else:
                    host_info = self.all_configs.host_info

                automation_editor = AutomationsEditor(
                    configuration, full_cfg, host_info
                )
                try:
                    automation_editor.disable_automation(ids_list)
                except Exception as exp:
                    print(exp)

    def del_addons(self):
        ids_list: list[str] = self.all_instructions.delete_addons.ids_list
        for addon_id in ids_list:
            try:
                addon_editor = AddonsEditor(self.all_configs.ssh_commands)
                addon_editor.use_ssh_addon(
                    addon_id, self.all_configs.ssh_commands.delete_addons
                )
            except Exception as exp:
                print(exp)

    def change_cfg_addons(self):
        addons_cfg_list: list[ChangeCfgAddons] = self.all_instructions.change_addons_cfg
        for addon_cfg in addons_cfg_list:
            try:
                # TODO: need to update
                addon_editor = AddonsEditor(self.all_configs.ssh_commands)
                new_cfg_path = addon_cfg.new_cfg_path + addon_cfg.id_addon
                cfg_name = "/config.yaml"

                addon_editor.write_new_cfg(new_cfg_path, cfg_name, addon_cfg.new_cfg)
                addon_editor.use_ssh_addon(
                    addon_cfg.id_addon, self.all_configs.ssh_commands.change_cfg_addons + [new_cfg_path + cfg_name]
                )
            except Exception as exp:
                print(exp)

    def disable_addons(self):
        ids_list: list[str] = self.all_instructions.disable_addons.ids_list
        for addon_id in ids_list:
            try:
                addon_editor = AddonsEditor(self.all_configs.ssh_commands)
                addon_editor.use_ssh_addon(
                    addon_id, self.all_configs.ssh_commands.disable_addons
                )
            except Exception as exp:
                print(exp)

    def del_script(self):
        for instruction in self.all_instructions.delete_script:

            full_cfg = self.file_io.read_with_type(instruction.path)
            script_editor = ScriptsEditor(full_cfg)

            for script_id in instruction.scripts_ids:
                try:
                    script_editor.delete_scripts(script_id)

                except Exception as exp:
                    print(exp)

            self.file_io.write_with_type(instruction.path, script_editor.edit_file)

    def del_script_restore_state(self):
        restore_path = (
            self.all_configs.config_restore_state.path
            + self.all_configs.config_restore_state.filename
        )
        full_cfg = self.file_io.read_with_type(
            restore_path, self.all_configs.config_restore_state.type_cfg
        )
        restore_script = EditorRestoreFile(
            self.all_configs.config_restore_state, full_cfg
        )

        for instruction in self.all_instructions.delete_script:

            try:
                restore_script.del_script_restore_state(instruction.scripts_ids)

            except Exception as exp:
                print(exp)

        self.file_io.write_with_type(
            restore_path,
            restore_script.full_cfg,
            self.all_configs.config_restore_state.type_cfg,
        )

    def del_objects(self):
        fl_fld_editor = FileFoldersEditor()
        for delete_object in self.all_instructions.delete_objects:
            for object_name in delete_object.objects_names:
                path = delete_object.path + "/" + object_name
                try:
                    fl_fld_editor.delete_objects(path)
                except Exception as exp:
                    print(exp)

    def clean_folders(self):
        fl_fld_editor = FileFoldersEditor()
        for delete_object in self.all_instructions.clean_folders:
            for object_name in delete_object.folders_names:
                path = delete_object.path + "/" + object_name
                try:
                    fl_fld_editor.clean_folders(path)
                except Exception as exp:
                    print(exp)

    def clean_files(self):
        fl_fld_editor = FileFoldersEditor()
        for delete_object in self.all_instructions.clean_files:
            for object_name in delete_object.files_names:
                path = delete_object.path + "/" + object_name
                try:
                    fl_fld_editor.clean_files(path)
                except Exception as exp:
                    print(exp)

    def change_files(self):
        for file_info in self.all_instructions.change_files:
            try:
                orig_file = self.file_io.read_with_type(file_info.path)
                file_editor = ScriptsEditor(orig_file)
                for new_part in file_info.new_content:
                    file_editor.change_file(new_part)
                self.file_io.write_with_type(file_info.path, file_editor.original_file)
            except Exception as exp:
                print(exp)

    def searching_in_files(self):
        searcher = FindInAllFiles()
        find_dict = searcher.start_find(
            self.all_instructions.find_in_all_files.text_to_find
        )
        if self.all_instructions.find_in_all_files.report_path:
            self.file_io.json_write(
                self.all_instructions.find_in_all_files.report_path, find_dict
            )
