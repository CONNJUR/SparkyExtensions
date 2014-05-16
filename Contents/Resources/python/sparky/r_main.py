import sparky
from . import r_model as model
from subprocess import Popen, PIPE
import os



class GitRepo(object):

    def __init__(self):
        self._path = model.project().sparky_directory
        # self._path = os.path.expanduser("~") + path
    
    def check_repo(self):
        os.chdir(self._path)
        p = Popen(["git", "status"], stdout=PIPE, stderr=PIPE)
        p.wait()
        return p
    
    def dump(self, commit_message):
        p = self.check_repo()
        if p.returncode != 0:
            raise ValueError("not a git repo: " + p.stderr.read())
        os.chdir(self._path)
        try:
            add = Popen(["git", "add", "Projects/", "Save/"], stdout=PIPE, stderr=PIPE)
            add.wait()
            if add.returncode != 0:
                raise ValueError("git add failed (" + add.stderr.read() + ")")
            commit = Popen(["git", "commit", "-m", commit_message], 
                           stdout=PIPE, 
                           stderr=PIPE)
            commit.wait()
            if commit.returncode != 0:
                raise ValueError("git commit failed (" + commit.stderr.read() + ", " + commit.stdout.read() + ")")
        except Exception, e:
            print 'failure making Sparky/git repository snapshot', e
            raise




import tkutil
import sputil
import r_peaktypes as peaktypes


class Snapshot_dialog(tkutil.Dialog):

    def __init__(self, session):
        self.g = GitRepo()
        
        self.session = session
        self.title = 'Snapshot'
        
        tkutil.Dialog.__init__(self, session.tk, self.title)
        
        br = tkutil.button_row(self.top, ('Make snapshot', self.make_snapshot))
        br.frame.pack(side='top', anchor='w')
        # TODO would like to get an enumerated list of these from somewhere
        e = tkutil.entry_field(self.top, 'Deductive reason used:', '<enter reason>', 50)
        e.frame.pack(side='top', anchor='w')
        self.message = e.variable

        br2 = tkutil.button_row(self.top, ('Set groups of selected peaks', self.set_group))
        br2.frame.pack(side = 'top', anchor = 'w')
        e2 = tkutil.entry_field(self.top, 'Group name:', '', 20, '(leave blank for name to be autogenerated)')
        e2.frame.pack(side = 'top', anchor = 'w')
        self.group = e2.variable

        br3 = tkutil.button_row(self.top, ('Set group-residue assignment', self.set_group_residue))
        br3.frame.pack(side='top', anchor='w')
        e3 = tkutil.entry_field(self.top, 'Group name:', '', 20)
        e3.frame.pack(side='top', anchor='w')
        e3_2 = tkutil.entry_field(self.top, 'Residue name:', '', 20)
        e3_2.frame.pack(side='top', anchor='w')
        self.group_name = e3.variable
        self.residue_name = e3_2.variable

        br4 = tkutil.button_row(self.top, ('Set resonance assignment', self.set_resonance_atomtype))
        br4.frame.pack(side='top', anchor='w')
        e4_1 = tkutil.entry_field(self.top, 'Group name:', '', 20)
        e4_1.frame.pack(side='top', anchor='w')
        e4_2 = tkutil.entry_field(self.top, 'Resonance name:', '', 20)
        e4_2.frame.pack(side='top', anchor='w')
        e4_3 = tkutil.entry_field(self.top, 'Atom:', '', 20)
        e4_3.frame.pack(side='top', anchor='w')
        self.res_group_name = e4_1.variable
        self.res_resonance_name = e4_2.variable
        self.res_atom = e4_3.variable

        br7 = tkutil.button_row(self.top, ('Set sequential group assignment', self.set_seq_ss))
        br7.frame.pack(side='top', anchor='w')
        e7 = tkutil.entry_field(self.top, 'Previous group name:', '', 20)
        e7.frame.pack(side='top', anchor='w')
        e7_2 = tkutil.entry_field(self.top, 'Following group name:', '', 20)
        e7_2.frame.pack(side='top', anchor='w')
        self.seq_ss_prev = e7.variable
        self.seq_ss_next = e7_2.variable

        br5 = tkutil.button_row(self.top, ('Set selected peaks to noise', self.set_noise))
        br5.frame.pack(side = 'top', anchor = 'w')

        br6 = tkutil.button_row(self.top, ('Set selected peaks to artifact', self.set_artifact))
        br6.frame.pack(side = 'top', anchor = 'w')
        
        self.peaktype_spectrum = m1 = tkutil.option_menu(self.top, 'Select peaktype spectrum', peaktypes.spectra.keys())
        m1.frame.pack(side='top', anchor='w')
        m1.add_callback(self.set_peaktype_spectrum)
        
        self.peaktype = m2 = tkutil.option_menu(self.top, 'Assign peaktype', [])
        m2.frame.pack(side='top', anchor='w')
        m2.add_callback(self.assign_peaktype)
#        m1.add_callback(self.assign_peaktype)




    def make_snapshot(self):
        self.g.dump(self.message.get())
    
    def set_group(self):
        name = self.group.get()
        if name == '':
            model.set_new_group()
        else:
            model.set_group(name)
    
    def set_noise(self):
        model.set_noise()
    
    def set_artifact(self):
        model.set_artifact()
    
    def set_group_residue(self):
        model.set_residue(self.group_name.get(), self.residue_name.get())
    
    def set_resonance_atomtype(self):
        model.set_atomtype(self.res_group_name.get(), 
                           self.res_resonance_name.get(), 
                           self.res_atom.get())
    
    def set_seq_ss(self):
        model.set_seq_ss(self.seq_ss_prev.get(), 
                         self.seq_ss_next.get())

    def set_peaktype_spectrum(self, spectrum):
        self.peaktype.remove_all_entries()
        for pt in peaktypes.spectra[spectrum]:
            self.peaktype.add_entry(','.join(pt))
    
    def assign_peaktype(self, peaktype):
        model.assign_peaktype(peaktype.split(','))



def show_snapshot_dialog(session):
    d = sputil.the_dialog(Snapshot_dialog, session)
    d.show_window(1)
