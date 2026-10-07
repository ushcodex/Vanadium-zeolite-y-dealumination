from pathlib import Path
from docx import Document
from docx.shared import Inches,Pt,Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
root=Path(__file__).resolve().parents[1]; out=root/'deliverables'
plt.rcParams.update({'font.family':'DejaVu Serif','font.size':10})
fig,ax=plt.subplots(figsize=(5.7,2.6)); ax.barh(['Water','Vanadic acid'],[-92.20,-106.69],color=['#477f9b','#a65a39']); ax.set_xlabel('Electronic adsorption energy (kJ mol⁻¹)'); ax.set_xlim(-130,0); fig.tight_layout();fig.savefig(out/'adsorption.png',dpi=220);plt.close(fig)
fig,ax=plt.subplots(figsize=(6,2.8)); x=['Complex','Intermediate I1','Saddle TS2','Intermediate I2','Product']; y=[-196.90,-385.10,-224.40,-342.36,-82.90];ax.scatter(range(5),y,color='#a65a39',s=60);ax.plot(range(5),y,color='#aaa',ls=':');ax.set_xticks(range(5),x,rotation=15);ax.set_ylabel('Relative electronic energy (kJ mol⁻¹)');fig.tight_layout();fig.savefig(out/'pathway.png',dpi=220);plt.close(fig)
d=Document(); sec=d.sections[0];sec.page_height=Cm(29.7);sec.page_width=Cm(21);sec.left_margin=Cm(3.8);sec.right_margin=Cm(2.5);sec.top_margin=Cm(2.5);sec.bottom_margin=Cm(2.5)
styles=d.styles; normal=styles['Normal'];normal.font.name='Times New Roman';normal.font.size=Pt(12);normal.paragraph_format.line_spacing=2;normal.paragraph_format.space_after=Pt(0)
for name,size in [('Title',14),('Heading 1',13),('Heading 2',12)]:
 st=styles[name];st.font.name='Times New Roman';st.font.size=Pt(size);st.font.bold=True;st.paragraph_format.space_before=Pt(12);st.paragraph_format.space_after=Pt(6)
in_refs=False
for line in (out/'thesis.md').read_text().splitlines():
 if not line.strip():continue
 if line.startswith('[FIGURE:'):
  path,caption=line[8:-1].split('|',1);p=d.add_paragraph();p.alignment=1;p.add_run().add_picture(str(root/'figures'/path),width=Inches(5.5));p=d.add_paragraph(caption);p.alignment=1;continue
 if line.startswith('[CHART:'):
  path,caption=line[7:-1].split('|',1);p=d.add_paragraph();p.alignment=1;p.add_run().add_picture(str(out/(path+'.png')),width=Inches(5.5));p=d.add_paragraph(caption);p.alignment=1;continue
 if line.startswith('[TABLE:'):
  caption,heads,*rows=line[7:-1].split('|');d.add_paragraph(caption); data=[heads.split(';')]+[r.split(';') for r in rows]; t=d.add_table(rows=0, cols=len(data[0]));t.style='Table Grid';t.alignment=WD_TABLE_ALIGNMENT.CENTER
  for row in data:
   cells=t.add_row().cells
   for c,value in zip(cells,row):
    c.text=value
    for p in c.paragraphs:
     p.paragraph_format.line_spacing=1.15
     for run in p.runs:run.font.name='Times New Roman';run.font.size=Pt(11)
  continue
 if line.startswith('# '):
  in_refs=(line=='# REFERENCES')
  if len(d.paragraphs)>1:d.add_page_break()
  d.add_paragraph(line[2:],style='Heading 1');continue
 if line.startswith('## '):d.add_paragraph(line[3:],style='Heading 2');continue
 p=d.add_paragraph();p.paragraph_format.first_line_indent=Cm(0.8)
 if line.startswith(('Figure ','Table ')) :p.paragraph_format.first_line_indent=Cm(0)
 r=p.add_run(line.replace('*',''))
 if d.paragraphs and any('REFERENCES' in q.text for q in d.paragraphs[-3:]):pass
 # bibliography recognition by author-year line after references heading
 if in_refs:
  p.paragraph_format.first_line_indent=Cm(-0.7);p.paragraph_format.left_indent=Cm(0.7);p.paragraph_format.line_spacing=1.15
  for run in p.runs:run.font.size=Pt(11)
footer=sec.footer.paragraphs[0];footer.alignment=WD_ALIGN_PARAGRAPH.CENTER
fld=OxmlElement('w:fldSimple');fld.set(qn('w:instr'),'PAGE');footer._p.append(fld)
d.save(out/'thesis.docx')
