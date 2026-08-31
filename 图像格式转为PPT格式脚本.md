# 使用codex的这个会话 01a047b7-0024-79d3-b586-86c7e8f1acb1 解决


这条固定 Python 渲染链会自动执行 `xelatex -> bibtex -> xelatex -> xelatex`，把中间文件全部收进 `.latex-cache/`，只在项目根目录保留 `main.pdf`。前两轮 XeLaTeX 只更新引用所需的 XDV/辅助文件，最后一轮才生成 PDF 和 SyncTeX。

`figures/` 中的 PNG 保留为原始图像，正文引用同名 PDF 副本。这些 PDF 只封装原 PNG 像素，不会转为 JPEG 或降采样，但可避免 `xdvipdfmx` 在每次编译时重新压缩图像。若更换某张 PNG，需同步重新生成它的同名 PDF。

在项目根目录可用下列命令批量重新封装；临时日志会留在 `.latex-cache/figure-pdf-wrap/`：

```bash
set -e
mkdir -p .latex-cache/figure-pdf-wrap
pdftex_bin="$(kpsewhich -var-value=SELFAUTOLOC)/pdftex"
for png in figures/*.png; do
  stem="$(basename "${png%.png}")"
  "$pdftex_bin" -interaction=batchmode -halt-on-error \
    -output-directory=.latex-cache/figure-pdf-wrap -jobname="$stem" \
    "\pdfximage{$png}\setbox0=\hbox{\pdfrefximage\pdflastximage}\pdfpagewidth=\wd0\pdfpageheight=\ht0\hoffset=-1in\voffset=-1in\shipout\box0\end"
  cp ".latex-cache/figure-pdf-wrap/$stem.pdf" "figures/$stem.pdf"
done