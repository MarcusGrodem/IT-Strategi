#!/usr/bin/env zsh
set -u

RUN_DIR="reports/webscraping_runs/2026-05-03_1619_coop_competitor_analysis"
URLS_FILE="$RUN_DIR/logs/source_urls.tsv"
RAW_DIR="$RUN_DIR/raw_sources"
LOG_FILE="$RUN_DIR/logs/crawl.log"
ACCESS_DATE="$(date '+%Y-%m-%d')"

: > "$LOG_FILE"

tail -n +2 "$URLS_FILE" | while IFS=$'\t' read -r slug url publisher source_type notes; do
  tmp_file="$RAW_DIR/${slug}.tmp.md"
  out_file="$RAW_DIR/${slug}.md"
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] crawling $slug $url" | tee -a "$LOG_FILE"
  if crwl "$url" -o markdown -O "$tmp_file" >> "$LOG_FILE" 2>&1; then
    {
      printf -- "---\n"
      printf "source_url: \"%s\"\n" "$url"
      printf "access_date: \"%s\"\n" "$ACCESS_DATE"
      printf "publisher: \"%s\"\n" "$publisher"
      printf "source_type: \"%s\"\n" "$source_type"
      printf "notes: \"%s\"\n" "$notes"
      printf -- "---\n\n"
      cat "$tmp_file"
    } > "$out_file"
    rm -f "$tmp_file"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ok $slug" | tee -a "$LOG_FILE"
  else
    {
      printf -- "---\n"
      printf "source_url: \"%s\"\n" "$url"
      printf "access_date: \"%s\"\n" "$ACCESS_DATE"
      printf "publisher: \"%s\"\n" "$publisher"
      printf "source_type: \"%s\"\n" "$source_type"
      printf "notes: \"crawl failed; see logs/crawl.log\"\n"
      printf -- "---\n\n"
      printf "# Crawl failed\n\nCrawl4AI could not extract this source during the run. See logs/crawl.log.\n"
    } > "$out_file"
    rm -f "$tmp_file"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] failed $slug" | tee -a "$LOG_FILE"
  fi
  sleep 2
done
