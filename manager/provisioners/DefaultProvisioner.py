from provisioners import BaseProvisioner
import wtferrors

class DefaultProvisioner(BaseProvisioner.BaseProvisioner):
  def __init__(self, module_info):
    super(DefaultProvisioner,self).__init__(module_info)

  def install(self):
    self._run_function("install")

  def remove(self):
    self._run_function("remove")


  def _run_function(self, func_name):
    func = self.module_info.get(func_name, {})
    if func == None:
      raise wtferrors.NotImplemented(func_name, "DefaultProvisioner", self.get_name())
    else:
      print("Running '{}' tasks for module '{}'...".format(func_name, self.get_name()))
      for task in func:      
        self._run_task(task, func_name)

  def _run_task(self, task, func):
    task_type = None

    for key in task:
      if key.lower() == "name":
        print("Task Name: {}".format(task.get(key)))
      else:
        task_type = key
        print("---> Running: {}".format(task_type))
        break

    mod = __import__("plugins.{}".format(task_type), fromlist=[task_type])
    klass = getattr(mod, task_type)
    runner = klass()

    if hasattr(runner, func) and callable(getattr(runner, func)):
      method_to_call = getattr(runner, func)      
      result, msg = method_to_call(task.get(task_type))
      if result:
        print("     + changed")
      else:
        print("     X no change")
      if msg is not None:
        print("       {}".format(msg))

    else:
      raise wtferrors.MissingFunction(func, task_type)