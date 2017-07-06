import json

def open_settings():
    with open('audioConfigs/audio_settings.json', 'r') as f:
        return json.loads(f.read())


def get_base_template():
    with open('audioConfigs/plugins/base.template', 'r') as f:
        return f.read()


def update_config(effect):
    template = effect["template_path"]
    with open(template, 'r') as f:
        temp = f.read()
    temp = temp.replace('$NEXT', effect["next"])
    for setting, value in effect["settings"].iteritems():
        temp = temp.replace(setting, value)
    return temp


if __name__ == '__main__':
    base_template = get_base_template()
    settings = open_settings()
    order = settings["order"]
    base_template = base_template.replace('$NEXT', '{0}:{1}'.format('plug', settings[order[0]]["alsa_alias"]))
    for idx, setting in enumerate(order):
        try:
            settings[setting]["next"] = settings[order[idx+1]]["alsa_alias"]
        except IndexError:
            settings[setting]["next"] = "plug:dmix"
        base_template += update_config(settings[setting])
    with open('/home/pi/.asoundrc', 'w') as f:
        f.write(base_template)
    
